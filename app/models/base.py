# app/models/base.py
import enum
from datetime import datetime, timezone
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.ext.asyncio import AsyncAttrs

# Utilizamos AsyncAttrs para habilitar la carga perezosa asíncrona (lazy loading) si se llegase a requerir
class Base(AsyncAttrs, DeclarativeBase):
    """
    Base declarativa maestra para SQLAlchemy 2.0.
    """
    pass

class TipoActa(str, enum.Enum):
    VEHICULO = "VEHICULO"
    COMERCIO = "COMERCIO"
    ACTIVIDAD = "ACTIVIDAD"

class EstadoActa(str, enum.Enum):
    EMITIDA = "EMITIDA"
    ANULADA = "ANULADA"
    OBSERVADA = "OBSERVADA" # Para contingencias o fiscalizaciones preventivas