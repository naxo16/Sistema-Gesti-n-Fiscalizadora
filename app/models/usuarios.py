import uuid
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base

class Rol(Base):
    __tablename__ = 'roles'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, unique=True, index=True)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    rol_id: Mapped[int] = mapped_column(ForeignKey('roles.id'))
    
    rol: Mapped["Rol"] = relationship()

class UsuarioMfa(Base):
    __tablename__ = 'usuario_mfa'
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    usuario_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('usuarios.id'), unique=True)
    totp_secret_encrypted: Mapped[str] = mapped_column(String)
    enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    confirmed_at: Mapped[str | None] = mapped_column(String, nullable=True) # or DateTime
    recovery_codes_encrypted: Mapped[str | None] = mapped_column(String, nullable=True)

class DispositivoMovil(Base):
    __tablename__ = 'dispositivos_moviles'
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    usuario_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('usuarios.id'))
    device_id: Mapped[str] = mapped_column(String, unique=True, index=True)
    nombre_dispositivo: Mapped[str] = mapped_column(String, nullable=True)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    revocado: Mapped[bool] = mapped_column(Boolean, default=False)
    estado: Mapped[str] = mapped_column(String(20), default='ACTIVO')
    last_seen_at: Mapped[str] = mapped_column(String, nullable=True)
