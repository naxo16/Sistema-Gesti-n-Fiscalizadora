import asyncio
import logging
from sqlalchemy import text
from app.core.database import AsyncSessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_anonymization():
    """
    Servicio de anonimización asíncrona según la Ley 21.719.
    Busca registros de actas cerradas o pagadas (estado_acta = 'DESPACHADA_JPL')
    y limpia nombre y RUT del infractor si han pasado más de 3 años (o el periodo definido).
    """
    logger.info("Iniciando tarea de anonimización de datos (Ley 21.719)...")
    async with AsyncSessionLocal() as session:
        try:
            # Query para infracciones vehiculares
            # Se usa un intervalo de 3 años como ejemplo de prescripción
            query = text("""
                UPDATE infracciones_vehiculares
                SET nombre_completo = NULL, rut_infractor = NULL
                FROM registros_base
                WHERE infracciones_vehiculares.registro_uuid = registros_base.id
                AND registros_base.estado = 'DESPACHADA_JPL'
                AND registros_base.fecha_emision < NOW() - INTERVAL '3 YEARS';
            """)
            
            result = await session.execute(query)
            await session.commit()
            
            logger.info(f"Tarea completada. Registros anonimizados: {result.rowcount}")
        except Exception as e:
            await session.rollback()
            logger.error(f"Error durante la anonimización: {e}")

if __name__ == "__main__":
    asyncio.run(run_anonymization())
