from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.repositories.auth_repository import AuthRepository
from app.core.security import create_access_token, verify_password
from app.schemas.auth import TokenResponse, LoginRequest

router = APIRouter()
auth_repo = AuthRepository()

@router.post("/login", response_model=TokenResponse)
async def login_for_access_token(
    request_data: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Endpoint para autenticación de inspectores desde Flutter.
    Recibe credenciales en formato JSON (username/password) y retorna un JWT.
    """
    user = await auth_repo.get_user_by_username(db, username=request_data.username)
    
    # Validamos las credenciales utilizando bcrypt.
    if not user or not verify_password(request_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Emitimos el JWT colocando el ID del usuario en el claim 'sub'
    access_token = create_access_token(data={"sub": str(user.id)})
    return TokenResponse(access_token=access_token, token_type="bearer")