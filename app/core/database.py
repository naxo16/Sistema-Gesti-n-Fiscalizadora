# -*- coding: utf-8 -*-
"""
Configuracion de la base de datos con SQLAlchemy asincro
"""
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.core.config import settings

# Motor asíncrono con pool de conexiones optimizado
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,          # Cambiar a True para ver el SQL generado en consola (solo en Dev)
    future=True,
    pool_size=20,        # Conexiones concurrentes máximas
    max_overflow=10
)
AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    autocommit=False, 
    autoflush=False, 
    expire_on_commit=False,
    class_=AsyncSession
)
Base = declarative_base()

# Inyección de Dependencia para FastAPI
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
