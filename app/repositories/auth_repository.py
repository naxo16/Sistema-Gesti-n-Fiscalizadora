from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.usuarios import Usuario

class AuthRepository:
    """
    Repositorio encargado de las consultas a la base de datos relacionadas
    con la autenticación y usuarios.
    """
    
    async def get_user_by_username(self, db: AsyncSession, username: str) -> Usuario | None:
        """
        Obtiene un usuario a partir de su username utilizando sintaxis moderna de SQLAlchemy 2.0.
        """
        stmt = select(Usuario).where(Usuario.username == username)
        return await db.scalar(stmt)
