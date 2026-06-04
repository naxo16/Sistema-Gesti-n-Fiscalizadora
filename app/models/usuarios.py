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
