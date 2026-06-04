import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

# Configuración mock temporal para el MVP
SECRET_KEY = "fiscalis_mvp_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 días para operación Offline extendida

# Contexto criptográfico usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica si la contraseña plana coincide con el hash almacenado."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Genera el hash seguro (bcrypt) de una contraseña."""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    """Genera un token JWT firmado."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt