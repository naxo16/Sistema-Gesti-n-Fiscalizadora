import uuid
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

# Convención de nombres para restricciones (Constraints)
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

class Base(DeclarativeBase):
    """
    Clase base para todos los modelos SQLAlchemy 2.0.
    """
    metadata = MetaData(naming_convention=convention)

import enum

class TipoActa(str, enum.Enum):
    VEHICULO = 'VEHICULO'
    COMERCIO = 'COMERCIO'
    ACTIVIDAD = 'ACTIVIDAD'

class EstadoActa(str, enum.Enum):
    BORRADOR = 'BORRADOR'
    PENDIENTE_SYNC = 'PENDIENTE_SYNC'
    SINCRONIZADO = 'SINCRONIZADO'
    EMITIDA = 'EMITIDA'
    ANULADA = 'ANULADA'