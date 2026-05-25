from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.api.deps import get_db
from app.schemas.auth import LoginRequest, Token
from app.models.infracciones import Dispositivo # Asegúrate de tener este modelo
from app.core.security import create_access_token

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_dispositivo(
    payload: LoginRequest, 
    db: AsyncSession = Depends(get_db)
):
    # 1. Validar si el dispositivo existe en la DB
    stmt = select(Dispositivo).where(Dispositivo.imei_hash == payload.imei_hash)
    result = await db.execute(stmt)
    dispositivo = result.scalar_one_or_none()

    if not dispositivo or not dispositivo.activo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Dispositivo no registrado o inactivo"
        )

    # 2. Generar Token JWT
    access_token = create_access_token(subject=dispositivo.imei_hash)
    return {"access_token": access_token, "token_type": "bearer"}