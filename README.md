# SGF Backend

Sistema de Gestion Fiscalizadora - Backend con FastAPI

## Estructura del Proyecto

```
sgf_backend/
│
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py       # Variables de entorno
│   │   └── database.py     # Motor SQLAlchemy Asincro
│   ├── models/
│   │   ├── __init__.py
│   │   └── base.py         # Clase Declarativa Base
│   ├── api/
│   │   └── v1/             # Routers
│   └── main.py             # Instancia de FastAPI
│
├── .env                    # Variables de entorno
├── requirements.txt        # Dependencias
└── alembic.ini             # Configuracion de migraciones
```

## Instalacion

1. Crear entorno virtual:
   python -m venv venv
   venv\Scripts\activate

2. Instalar dependencias:
   pip install -r requirements.txt

3. Configurar .env con tus credenciales

4. Inicializar Alembic:
   alembic init alembic

## Correr la aplicacion

uvicorn app.main:app --reload
