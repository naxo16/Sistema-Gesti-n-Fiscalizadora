# -*- coding: utf-8 -*-
"""
Configuracion de la base de datos con SQLAlchemy asincro
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Motor asincro
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True
)

# Session factory
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    """Dependencia para obtener sesion de base de datos"""
    async with async_session() as session:
        yield session
