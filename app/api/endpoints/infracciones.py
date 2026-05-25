from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
import logging
from app.services.archivos import ArchivosService
from app.models.infracciones import Evidencia
import uuid
from app.schemas.infracciones import ActaRegistroCreate, ActaRegistroResponse
from app.repositories.infracciones import ActaRegistroRepository
from app.api.deps import get_db, get_dispositivo_actual

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post(
    "/sync", 
    response_model=ActaRegistroResponse, 
    status_code=status.HTTP_201_CREATED,
    summary="Sincroniza un acta de infracción desde terreno"
)
async def sync_infraccion(
    payload: ActaRegistroCreate,
    imei_hash: Annotated[str, Depends(get_dispositivo_actual)],
    db: Annotated[AsyncSession, Depends(get_db)]
) -> ActaRegistroResponse:
    
    repository = ActaRegistroRepository(db)
    
    try:
        acta_sincronizada = await repository.sincronizar_acta(payload)
        logger.info(f"Acta {payload.id} sincronizada correctamente por dispositivo {imei_hash}")
        return acta_sincronizada
        
    except ValueError as ve:
        # Aquí usamos payload.id y agregamos el imei_hash para auditoría
        logger.warning(f"Validación fallida (422) del dispositivo {imei_hash} en acta {payload.id}: {str(ve)}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Datos de acta inválidos o violan regla de negocio: {str(ve)}"
        )
        
    except Exception as e:
        # Error 500 para gatillar el Backoff en Flutter
        logger.error(f"Fallo sistémico (500) del dispositivo {imei_hash} sincronizando acta {payload.id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del validador central. Aplique Exponential Backoff."
        )

@router.post(
    "/{acta_id}/evidencias", 
    status_code=status.HTTP_201_CREATED,
    summary="Adjunta una fotografía forense a un acta existente"
)
async def upload_evidencia(
    acta_id: uuid.UUID,
    imei_hash: Annotated[str, Depends(get_dispositivo_actual)],
    db: Annotated[AsyncSession, Depends(get_db)],
    file: UploadFile = File(...) # <--- ¡Lo movimos al final!
):
    try:
        # 1. Guardar físicamente y obtener metadatos seguros
        metadatos = await ArchivosService.procesar_y_guardar_evidencia(str(acta_id), file)
        
        # 2. Persistir metadatos en PostgreSQL
        nueva_evidencia = Evidencia(
            acta_id=acta_id,
            ruta_archivo=metadatos["ruta_archivo"],
            mime_type=metadatos["mime_type"],
            peso_bytes=metadatos["peso_bytes"],
            hash_sha256=metadatos["hash_sha256"]
        )
        
        db.add(nueva_evidencia)
        await db.commit()
        await db.refresh(nueva_evidencia)
        
        logger.info(f"Evidencia {nueva_evidencia.id} adjuntada al acta {acta_id} por {imei_hash}")
        
        return {
            "id": nueva_evidencia.id,
            "status": "Evidencia guardada y validada forensemente",
            "hash_sha256": nueva_evidencia.hash_sha256
        }
        
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail=str(ve))
    except Exception as e:
        await db.rollback()
        logger.error(f"Fallo guardando evidencia para acta {acta_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Fallo en almacenamiento de disco.")
    
@router.get("/{id}", response_model=ActaRegistroResponse, summary="Consulta el estado de un acta")
async def get_acta_status(
    id: uuid.UUID,
    imei_hash: Annotated[str, Depends(get_dispositivo_actual)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    repository = ActaRegistroRepository(db)
    # Asumimos que necesitas un método en tu Repo para obtener por ID
    acta = await repository.obtener_por_id(id)
    
    if not acta:
        raise HTTPException(status_code=404, detail="Acta no encontrada")
        
    return acta