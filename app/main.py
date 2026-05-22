# -*- coding: utf-8 -*-
"""
Aplicacion principal FastAPI
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description="Backend para Sistema de Gestion Forestal"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Verificar que la API esta funcionando"""
    return {"status": "ok"}
