# app/repositories/infracciones.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert
import uuid
from app.models.infracciones import ActaRegistro, ActaVehiculo
from app.schemas.infracciones import ActaRegistroCreate


class ActaRegistroRepository:
    """
    Capa de Acceso a Datos orquestada para Actas de Fiscalización.
    Maneja persistencia atómica, idempotencia y conversiones espaciales PostGIS.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    async def sincronizar_acta(self, payload: ActaRegistroCreate) -> ActaRegistro:
        """
        Guarda un acta proveniente del cliente móvil de forma segura e idempotente.
        Si el ID (UUIDv4) ya existe en base de datos, omite la inserción y retorna el registro actual.
        """
        # 1. Transformación Espacial: WKT (Well-Known Text)
        # IMPORTANTE: PostGIS espera las coordenadas en orden LONGITUD (X) y luego LATITUD (Y).
        punto_wkt = f"SRID=4326;POINT({payload.ubicacion.lng} {payload.ubicacion.lat})"

        # 2. Construcción de la sentencia INSERT con ON CONFLICT (Dialecto PostgreSQL)
        stmt_registro = insert(ActaRegistro).values(
            id=payload.id,
            dispositivo_id=payload.dispositivo_id,
            tipo=payload.tipo,
            estado=payload.estado,
            fecha_emision=payload.fecha_emision,
            ubicacion=punto_wkt
        ).on_conflict_do_nothing(
            index_elements=['id'] # Si el ID ya existe, no hacemos NADA
        ).returning(ActaRegistro)

        # Ejecutamos la inserción del padre
        result_registro = await self.db.execute(stmt_registro)
        acta_insertada = result_registro.scalar_one_or_none()

        if acta_insertada is not None:
            # Escenario A: Es un registro NUEVO. Procedemos a insertar relaciones hijas si existen.
            if payload.vehiculo and payload.tipo.value == "VEHICULO":
                stmt_vehiculo = insert(ActaVehiculo).values(
                    id=payload.id, # PK y FK compartida (Relación 1:1 estricta)
                    patente=payload.vehiculo.patente,
                    marca_modelo=payload.vehiculo.marca_modelo,
                    color=payload.vehiculo.color
                ).on_conflict_do_nothing()
                
                await self.db.execute(stmt_vehiculo)
            
            # Confirmamos cambios a la DB
            await self.db.commit()
            await self.db.refresh(acta_insertada)
            return acta_insertada

        else:
            # Escenario B: IDEMPOTENCIA. El acta ya existía (ej: reintento de red del móvil).
            # Hacemos rollback de la transacción actual por seguridad.
            await self.db.rollback()
            
            # Buscamos el registro existente para devolverlo y calmar al cliente (HTTP 200)
            query_existente = select(ActaRegistro).where(ActaRegistro.id == payload.id)
            result_existente = await self.db.execute(query_existente)
            acta_existente = result_existente.scalar_one()
            
            return acta_existente
        
    async def obtener_por_id(self, id: uuid.UUID) -> ActaRegistro | None:
        """
        Consulta rápida para verificar el estado de un acta.
        Flutter usa esto para saber si el backend ya recibió y procesó el acta.
        """
        stmt = select(ActaRegistro).where(ActaRegistro.id == id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()