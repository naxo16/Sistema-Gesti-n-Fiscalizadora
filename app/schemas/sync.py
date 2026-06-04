from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Any
from datetime import datetime
import uuid

class EvidenciaSchema(BaseModel):
    hash_sha256: str = Field(..., description="Hash SHA-256 de la imagen de evidencia")
    
    model_config = ConfigDict(from_attributes=True)

class SincronizacionActaRequest(BaseModel):
    id: uuid.UUID
    rutInfractor: str | None = None
    nombreCompleto: str | None = None
    ppu: str
    tipoVehiculo: str | None = None
    marcaVehiculo: str | None = None
    colorVehiculo: str | None = None
    tipoInfraccionId: int | None = None
    coordenadas: str
    fotos: List[Any] = Field(default_factory=list)
    fecha: datetime
    descripcion: str | None = None
    firmaRechazo: bool = False
    status: str

    model_config = ConfigDict(from_attributes=True)
