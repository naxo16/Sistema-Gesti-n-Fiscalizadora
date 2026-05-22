# -*- coding: utf-8 -*-
"""
Aplicacion principal FastAPI
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Lógica de encendido (Startup)
    print("SGF Core Inicializando: Cargando motor de base de datos...")
    yield
    # Lógica de apagado (Shutdown)
    print("SGF Core Apagando: Cerrando conexiones...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
    description="Backend para Sistema de Gestion Fiscalización"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Infraestructura"])
async def health_check():
    """Verificar que la API esta funcionando"""
    return {
        "status": "ok",
        "system": settings.PROJECT_NAME,
        "version": settings.VERSION
        }
