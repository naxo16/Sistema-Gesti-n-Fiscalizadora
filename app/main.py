# -*- coding: utf-8 -*-
"""
Aplicacion principal FastAPI
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.endpoints import infracciones, auth

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

# CORS middleware (Corregido para seguridad)
app.add_middleware(
    CORSMiddleware,
    # Idealmente en producción: allow_origins=settings.BACKEND_CORS_ORIGINS
    allow_origins=["*"], 
    allow_credentials=False, # <-- Cambiado a False para permitir orígenes con "*"
    allow_methods=["*"],
    allow_headers=["*"],
)

# ENSAMBLAJE CRÍTICO: Registrar el router de infracciones
app.include_router(
    infracciones.router,
    prefix=f"{settings.API_V1_STR}/infracciones",
    tags=["Sincronización Offline-First"],
)
app.include_router(
    auth.router,
    prefix=f"{settings.API_V1_STR}/auth",
    tags=["Autenticación"]
)
@app.get("/health", tags=["Infraestructura"])
async def health_check():
    """Verificar que la API esta funcionando"""
    return {
        "status": "ok",
        "system": settings.PROJECT_NAME,
        "version": settings.VERSION
    }