# app/models/__init__.py
from app.models.base import Base, TipoActa, EstadoActa
from app.models.infracciones import Dispositivo, ActaRegistro, ActaVehiculo, AuditoriaEvento, Evidencia

# Esto asegura que cuando importes Base en alembic/env.py, 
# la metadata ya tenga el registro de todas las tablas definidas.
__all__ = ["Base", "TipoActa", "EstadoActa", "Dispositivo", "ActaRegistro", "ActaVehiculo", "AuditoriaEvento", "Evidencia"]