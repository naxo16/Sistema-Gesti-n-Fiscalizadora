import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.models.registros import InfraccionVehicular, EvidenciaFotografica
from app.schemas.sync import SincronizacionActaRequest

class SyncRepository:
    """
    Repositorio encargado de manejar la persistencia de los datos 
    provenientes de la sincronización Offline-First.
    """
    
    async def procesar_acta_vehicular(self, db: AsyncSession, payload: SincronizacionActaRequest, inspector_id: uuid.UUID) -> InfraccionVehicular:
        try:
            # 1. Transformación Geoespacial (PostGIS)
            # PostGIS requiere el orden: LONGITUD LATITUD
            ubicacion_wkt = f"SRID=4326;POINT({payload.longitud} {payload.latitud})"
            
            # 2. Instanciación Polimórfica
            # SQLAlchemy manejará automáticamente la inserción en 'registros_base' e 'infracciones_vehiculares'
            nueva_acta = InfraccionVehicular(
                id=payload.id,
                inspector_id=inspector_id,
                estado=payload.estado,
                fecha_emision=payload.fecha_emision,
                ubicacion=ubicacion_wkt,
                # Atributos específicos de la tabla hija
                ppu=payload.vehiculo.ppu,
                marca=payload.vehiculo.marca,
                tipo_vehiculo=payload.vehiculo.tipo_vehiculo,
                color=payload.vehiculo.color,
                tipo_infraccion_id=payload.vehiculo.tipo_infraccion_id,
                observaciones=payload.vehiculo.observaciones
            )
            
            db.add(nueva_acta)
            
            # 3. Manejo de Evidencias
            for evidencia_req in payload.evidencias:
                nueva_evidencia = EvidenciaFotografica(
                    registro_uuid=payload.id,
                    hash_sha256=evidencia_req.hash_sha256
                )
                db.add(nueva_evidencia)
                
            # 4. Transaccionalidad ACID
            await db.commit()
            return nueva_acta
            
        except IntegrityError as e:
            await db.rollback()
            # Se relanza para que sea manejada en la capa de servicios o el controlador (ej. duplicados)
            raise e
        except Exception as e:
            await db.rollback()
            raise e
