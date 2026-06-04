import uuid
from datetime import datetime, timezone
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.models.base import Base

class AuditoriaEvento(Base):
    __tablename__ = 'auditoria_eventos'
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entidad_id: Mapped[str] = mapped_column(String, index=True)
    entidad_tipo: Mapped[str] = mapped_column(String, index=True)
    accion: Mapped[str] = mapped_column(String)
    usuario_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey('usuarios.id'), nullable=True)
    payload: Mapped[dict] = mapped_column(JSONB)
    fecha: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

class SyncEvent(Base):
    __tablename__ = 'sync_events'
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    dispositivo_id: Mapped[str] = mapped_column(String, index=True)
    inspector_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('usuarios.id'))
    fecha_sync: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    estado: Mapped[str] = mapped_column(String)
    detalles: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
