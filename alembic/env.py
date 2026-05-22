import asyncio
from logging.config import fileConfig

from geoalchemy2 import alembic_helpers
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

from app.core.config import settings
# CORRECCIÓN 1: Importamos desde 'app.models' para que el __init__.py cargue TODAS las tablas en el metadata
from app.models import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Inyectamos la URL dinámica de nuestra base de datos (PostgreSQL)
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        # Opcional pero recomendado: reflejar las reglas también en offline
        compare_type=True,
        compare_server_default=True,
        include_object=alembic_helpers.include_object,
        process_revision_directives=alembic_helpers.writer,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    # CORRECCIÓN 2: Aquí es donde debe ir la configuración con la conexión inyectada
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,       # Detecta si cambiamos un String(50) a String(100)
        compare_server_default=True,
        include_object=alembic_helpers.include_object,      # Evita que Alembic borre tablas internas de PostGIS
        process_revision_directives=alembic_helpers.writer, # Directivas espaciales para Geometry
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context."""

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()