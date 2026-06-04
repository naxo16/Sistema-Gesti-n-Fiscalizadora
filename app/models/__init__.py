# app/models/__init__.py
from app.models.base import Base
from app.models.usuarios import Usuario, Rol
from app.models.registros import RegistroBase, InfraccionVehicular, EvidenciaFotografica
from app.models.auditoria import AuditoriaEvento, SyncEvent

# Esto asegura que cuando importes Base en alembic/env.py, 
# la metadata ya tenga el registro de todas las tablas definidas.
__all__ = [
    "Base", 
    "Usuario", 
    "Rol", 
    "RegistroBase", 
    "InfraccionVehicular", 
    "EvidenciaFotografica", 
    "AuditoriaEvento", 
    "SyncEvent"
]