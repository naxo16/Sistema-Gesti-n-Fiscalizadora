# app/schemas/infracciones.py
import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

from app.models.base import TipoActa, EstadoActa

class UbicacionMovil(BaseModel):
    """Coordenadas puras que envía el cliente móvil (Flutter)."""
    lat: float = Field(..., ge=-90, le=90, description="Latitud WGS84")
    lng: float = Field(..., ge=-180, le=180, description="Longitud WGS84")

class ActaVehiculoCreate(BaseModel):
    """Payload de especialización para vehículos"""
    patente: str = Field(..., min_length=4, max_length=10, description="Patente del vehículo")
    marca_modelo: Optional[str] = Field(None, max_length=100)
    color: Optional[str] = Field(None, max_length=50)

class ActaRegistroCreate(BaseModel):
    """Payload principal que recibe el endpoint de sincronización."""
    id: uuid.UUID = Field(..., description="UUIDv4 generado en el móvil")
    dispositivo_id: uuid.UUID = Field(..., description="ID del dispositivo que emite el acta")
    
    tipo: TipoActa
    estado: EstadoActa = Field(default=EstadoActa.EMITIDA)
    
    fecha_emision: datetime = Field(..., description="Timestamp exacto en terreno")
    ubicacion: UbicacionMovil
    
    vehiculo: Optional[ActaVehiculoCreate] = Field(None, description="Datos del vehículo si tipo=VEHICULO")

class ActaRegistroResponse(BaseModel):
    """Respuesta que se devuelve al móvil para confirmar la recepción."""
    id: uuid.UUID
    estado: EstadoActa
    fecha_recepcion_server: datetime
    version: int

    # Configuración de Pydantic V2 para leer directamente desde objetos SQLAlchemy
    model_config = ConfigDict(from_attributes=True)