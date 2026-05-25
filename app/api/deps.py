from typing import AsyncGenerator, Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

# CAMBIO CRÍTICO: Usamos PyJWT en lugar de python-jose
import jwt
from jwt.exceptions import InvalidTokenError

from app.core.database import AsyncSessionLocal
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/token")

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency Injection de la sesión de BD."""
    async with AsyncSessionLocal() as session:
        yield session

async def get_dispositivo_actual(token: Annotated[str, Depends(oauth2_scheme)]) -> str:
    """Validación Stateless del dispositivo mediante JWT o Token de Desarrollo."""
    
    # --- INICIO BYPASS DE DESARROLLO ---
    # Si Flutter envía este token exacto, lo dejamos pasar como un dispositivo de prueba
    if token == "dev-flutter-token-123":
        return "dispositivo_prueba_flutter_001"
    # --- FIN BYPASS ---

    credenciales_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de dispositivo inválidas o expiradas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        imei_hash: str | None = payload.get("sub")
        
        if imei_hash is None:
            raise credenciales_exception
        
        return imei_hash
        
    except InvalidTokenError: # Atrapamos la excepción específica de PyJWT
        raise credenciales_exception