import asyncio
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import select, text
from app.core.database import AsyncSessionLocal, engine
from app.models.base import Base
from app.models.usuarios import Usuario, Rol
from app.core.security import get_password_hash

async def seed_db():
    print("Iniciando proceso de seeder de base de datos...")
    
    print("[*] Limpiando dependencias antiguas y sincronizando nuevo esquema (Clean Architecture)...")
    async with engine.begin() as conn:
        # Usamos DROP CASCADE para eliminar dependencias viejas (como sesiones_moviles, registros)
        await conn.execute(text("DROP TABLE IF EXISTS usuarios CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS roles CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS registros_base CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS infracciones_vehiculares CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS evidencias_fotograficas CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS auditoria_eventos CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS sync_events CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS registros CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS vehiculos CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS evidencias CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS dispositivos CASCADE"))
        
        # Recreamos toda la arquitectura limpia
        await conn.run_sync(Base.metadata.create_all)
        
    async with AsyncSessionLocal() as session:
        try:
            # 1. Verificar o crear el Rol "inspector" (RBAC)
            stmt_rol = select(Rol).where(Rol.nombre == "inspector")
            rol = await session.scalar(stmt_rol)
            
            if not rol:
                print("[*] Creando rol 'inspector'...")
                rol = Rol(nombre="inspector")
                session.add(rol)
                await session.flush() 
            else:
                print("[*] El rol 'inspector' ya existe en el sistema.")

            # 2. Verificar o crear el Usuario
            username = "11111111-1"
            stmt_user = select(Usuario).where(Usuario.username == username)
            user = await session.scalar(stmt_user)

            if not user:
                print(f"[*] Creando usuario '{username}'...")
                plain_password = "Cauquenes.2026*"
                
                # HASHEAMOS LA CONTRASEÑA USANDO BCRYPT
                hashed_password = get_password_hash(plain_password)
                
                nuevo_usuario = Usuario(
                    username=username,
                    hashed_password=hashed_password,
                    rol_id=rol.id,
                    activo=True
                )
                session.add(nuevo_usuario)
                await session.commit()
                print("[+] ¡Usuario creado exitosamente con credenciales seguras (bcrypt)!")
            else:
                print(f"[*] El usuario '{username}' ya existe. Ignorando creación.")

        except Exception as e:
            await session.rollback()
            print(f"[!] Error durante la ejecución del seeder: {e}")

if __name__ == "__main__":
    asyncio.run(seed_db())
