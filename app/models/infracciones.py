# app/models/infracciones.py
import uuid
from datetime import datetime, timezone
from sqlalchemy import String, Integer, DateTime, ForeignKey, Boolean, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID, JSONB, ENUM
from geoalchemy2 import Geometry

from app.models.base import Base, TipoActa, EstadoActa

class Dispositivo(Base):
    """Gestión de seguridad perimetral stateless"""
    __tablename__ = "dispositivos"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    imei_hash: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    es_activo: Mapped[bool] = mapped_column(Boolean, default=True)
    
    # Relación Inversa (1:N)
    actas: Mapped[list["ActaRegistro"]] = relationship(back_populates="dispositivo", lazy="noload")

class ActaRegistro(Base):
    """Tabla Maestra (Source of Truth) con soporte Idempotente"""
    __tablename__ = "registros"

    # UUIDv4 generados en el Flutter (Offline-First), pero con default por seguridad.
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    dispositivo_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("dispositivos.id", ondelete="RESTRICT"), nullable=False)
    
    tipo: Mapped[TipoActa] = mapped_column(ENUM(TipoActa, name="tipo_acta_enum", create_type=False), nullable=False)
    estado: Mapped[EstadoActa] = mapped_column(ENUM(EstadoActa, name="estado_acta_enum", create_type=False), default=EstadoActa.EMITIDA)
    
    fecha_emision: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    fecha_recepcion_server: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Punto geográfico SRID 4326 (WGS 84 - GPS estándar)
    ubicacion: Mapped[str] = mapped_column(Geometry(geometry_type='POINT', srid=4326), nullable=False)

    # Bloqueo Optimista (Optimistic Concurrency Control)
    version: Mapped[int] = mapped_column(Integer, default=1, nullable=False)

    # Relaciones 1:1 Especializadas
    vehiculo: Mapped["ActaVehiculo"] = relationship(back_populates="registro_padre", cascade="all, delete-orphan", uselist=False)
    # Relación 1:N con Evidencias
    evidencias: Mapped[list["Evidencia"]] = relationship(back_populates="acta", cascade="all, delete-orphan")
    # Auditoría forense 1:N
    eventos_auditoria: Mapped[list["AuditoriaEvento"]] = relationship(back_populates="acta", cascade="all, delete-orphan")
    dispositivo: Mapped["Dispositivo"] = relationship(back_populates="actas")

    __mapper_args__ = {
        "version_id_col": version # SQLAlchemy gestionará automáticamente el incremento del campo en UPDATES
    }

class ActaVehiculo(Base):
    """Tabla Hija: Especialización 1:1 de Registros para Vehículos"""
    __tablename__ = "vehiculos"

    # La Primary Key también es Foreign Key (garantiza relación estricta 1:1)
    id: Mapped[uuid.UUID] = mapped_column(ForeignKey("registros.id", ondelete="CASCADE"), primary_key=True)
    patente: Mapped[str] = mapped_column(String(10), nullable=False, index=True)
    marca_modelo: Mapped[str | None] = mapped_column(String(100), nullable=True)
    color: Mapped[str | None] = mapped_column(String(50), nullable=True)

    registro_padre: Mapped["ActaRegistro"] = relationship(back_populates="vehiculo")

class AuditoriaEvento(Base):
    """Event Sourcing Inmutable (Append-Only) para trazabilidad legal"""
    __tablename__ = "auditoria_eventos"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    registro_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("registros.id", ondelete="CASCADE"), nullable=False, index=True)
    
    accion: Mapped[str] = mapped_column(String(50), nullable=False) # ej: "RECEPCION_LOTE", "CORRECCION_OFICIO"
    payload_snapshot: Mapped[dict] = mapped_column(JSONB, nullable=False) # Estado de la entidad en formato JSONB indexable
    
    fecha_evento: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    operador_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True) # Operador de backend que intervino, si aplica

    acta: Mapped["ActaRegistro"] = relationship(back_populates="eventos_auditoria")

class Evidencia(Base):
    """Almacenamiento de metadatos forenses de las fotografías/archivos"""
    __tablename__ = "evidencias"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    acta_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("registros.id", ondelete="CASCADE"), nullable=False, index=True)
    
    ruta_archivo: Mapped[str] = mapped_column(String(500), nullable=False) # Ruta física en el disco del servidor
    mime_type: Mapped[str] = mapped_column(String(100), nullable=False)    # ej: 'image/jpeg' verificado por MagicBytes
    peso_bytes: Mapped[int] = mapped_column(Integer, nullable=False)
    
    hash_sha256: Mapped[str] = mapped_column(String(64), nullable=False)   # Sello de inmutabilidad
    fecha_subida: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    acta: Mapped["ActaRegistro"] = relationship(back_populates="evidencias")