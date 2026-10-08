# -*- coding: utf-8 -*-
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request
# Ajustar importaciones para usar los routers recién creados
from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.infracciones import router as infracciones_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Lógica de encendido (Startup)
    print("SGF MVP Inicializando: Cargando motor de base de datos...")
    yield
    # Lógica de apagado (Shutdown)
    print("SGF MVP Apagando: Cerrando conexiones...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
    description="Backend para Sistema de Gestion Fiscalización - MVP"
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("="*50)
    print("❌ ERROR DE VALIDACIÓN (422) ❌")
    print("Cuerpo recibido:", exc.body)
    print("Errores detallados:", exc.errors())
    print("="*50)
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )

@app.middleware("http")
async def add_corp_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cross-Origin-Resource-Policy"] = "cross-origin"
    return response

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ENSAMBLAJE: Registrar el router de Autenticación
app.include_router(
    auth_router,
    prefix=f"{settings.API_V1_STR}/auth",
    tags=["Autenticación"]
)

# ENSAMBLAJE: Registrar el router de Sincronización e Infracciones
app.include_router(
    infracciones_router,
    prefix=f"{settings.API_V1_STR}/infracciones",
    tags=["Sincronización Offline-First"]
)

@app.get("/health", tags=["Infraestructura"])
async def health_check():
    """Verificar que la API esta funcionando"""
    return {
        "status": "ok",
        "system": settings.PROJECT_NAME,
        "version": settings.VERSION
    }