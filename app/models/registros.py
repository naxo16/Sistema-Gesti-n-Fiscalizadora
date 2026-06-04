import uuid
from typing import Any
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.models.base import Base
from app.models.usuarios import Usuario

class RegistroBase(Base):
    __tablename__ = 'registros_base'
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    inspector_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('usuarios.id'), index=True)
    modulo: Mapped[str] = mapped_column(String, index=True)
    estado: Mapped[str] = mapped_column(String, index=True)
    fecha_emision: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    ubicacion: Mapped[Any] = mapped_column(Geometry('POINT', srid=4326))
    
    __mapper_args__ = {
        "polymorphic_on": "modulo",
        "polymorphic_identity": "base",
    }
    
    inspector: Mapped["Usuario"] = relationship()

class InfraccionVehicular(RegistroBase):
    __tablename__ = 'infracciones_vehiculares'
    registro_uuid: Mapped[uuid.UUID] = mapped_column(ForeignKey('registros_base.id'), primary_key=True)
    ppu: Mapped[str] = mapped_column(String, index=True)
    rut_infractor: Mapped[str | None] = mapped_column(String, nullable=True)
    nombre_completo: Mapped[str | None] = mapped_column(String, nullable=True)
    marca: Mapped[str | None] = mapped_column(String, nullable=True)
    tipo_vehiculo: Mapped[str | None] = mapped_column(String, nullable=True)
    color: Mapped[str | None] = mapped_column(String, nullable=True)
    tipo_infraccion_id: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    observaciones: Mapped[str | None] = mapped_column(Text, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "infraccion_vehicular",
    }

class EvidenciaFotografica(Base):
    __tablename__ = 'evidencias_fotograficas'
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    registro_uuid: Mapped[uuid.UUID] = mapped_column(ForeignKey('registros_base.id'), index=True)
    hash_sha256: Mapped[str] = mapped_column(String)

    __table_args__ = (
        UniqueConstraint('registro_uuid', 'hash_sha256', name='uq_evidencia_registro_hash'),
    )
