import uuid
from typing import AsyncGenerator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
import jwt
from jwt.exceptions import InvalidTokenError

from app.core.database import AsyncSessionLocal
from app.core.security import SECRET_KEY, ALGORITHM

# Definición del esquema de autenticación esperado en Swagger/OpenAPI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency Injection de la sesión de base de datos."""
    async with AsyncSessionLocal() as session:
        yield session

async def get_current_inspector(token: str = Depends(oauth2_scheme)) -> uuid.UUID:
    """
    Decodifica el JWT, valida la firma y extrae el inspector_id.
    Si es inválido, retorna HTTP 401.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales o el token expiró",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        inspector_id: str | None = payload.get("sub")
        
        if inspector_id is None:
            raise credentials_exception
            
        return uuid.UUID(inspector_id)
        
    except (InvalidTokenError, ValueError):
        raise credentials_exception