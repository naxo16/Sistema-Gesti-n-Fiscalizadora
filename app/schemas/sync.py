from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime
import uuid

class EvidenciaSchema(BaseModel):
    hash_sha256: str = Field(..., description="Hash SHA-256 de la imagen de evidencia")
    
    model_config = ConfigDict(from_attributes=True)

class DatosVehicularesSchema(BaseModel):
    ppu: str = Field(..., description="Placa Patente Única")
    marca: str
    tipo_vehiculo: str
    color: str
    tipo_infraccion_id: str
    observaciones: str | None = None
    
    model_config = ConfigDict(from_attributes=True)

class SincronizacionActaRequest(BaseModel):
    id: uuid.UUID = Field(..., description="UUID generado en el dispositivo móvil")
    modulo: str = Field(..., description="Módulo de origen, ej: infraccion_vehicular")
    estado: str = Field(..., description="Estado de la infracción")
    fecha_emision: datetime = Field(..., description="Fecha y hora de emisión")
    latitud: float = Field(..., description="Latitud de la ubicación")
    longitud: float = Field(..., description="Longitud de la ubicación")
    
    # Datos específicos del acta vehicular
    vehiculo: DatosVehicularesSchema
    
    # Evidencias fotográficas asociadas
    evidencias: List[EvidenciaSchema] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
