# Context Engineering: Backend Rules

## Stack Tecnológico
- **Framework:** FastAPI
- **ORM:** SQLAlchemy 2.0 (Asíncrono)
- **Validación de Datos:** Pydantic V2
- **Migraciones:** Alembic

## Arquitectura
Se aplica una arquitectura estricta (Clean Architecture) con la siguiente estructura:
- `app/api`: Controladores y enrutamiento de endpoints.
- `app/core`: Configuración central (seguridad, base de datos, variables de entorno).
- `app/models`: Modelos ORM (SQLAlchemy).
- `app/schemas`: Modelos de validación (Pydantic).
- `app/services`: Lógica de negocio.

## Reglas de Seguridad (ISO 27001 y DERA)
- **Autenticación:** Todo endpoint debe requerir autenticación mediante token JWT, con la única excepción del endpoint de login.
- **Inyección de Base de Datos:** Las inyecciones de dependencias de la base de datos deben realizarse exclusivamente vía `Depends(get_db)`.
