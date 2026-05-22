# -*- coding: utf-8 -*-
"""
Configuracion del proyecto
Variables de entorno y settings globales
"""
from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    """Configuracion de la aplicacion"""
    # Base de Datos
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://user:password@localhost:5432/sgf_db"
    )

    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-this")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # API
    API_TITLE: str = "SGF Backend API"
    API_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
