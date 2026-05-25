SGF_CORE Backend

Sistema de Gestión Fiscalizadora (SGF_CORE) - Backend de alto rendimiento construido con FastAPI. Diseñado bajo principios de Clean Architecture para servir como motor validador en una solución distribuida Offline-First.
🚀 Tecnologías Clave

    Framework: FastAPI (Asíncrono)

    Base de Datos: PostgreSQL + PostGIS

    ORM: SQLAlchemy 2.0 (Asíncrono)

    Migraciones: Alembic

    Seguridad: JWT Stateless (con Bypass de desarrollo)

    Validación: Pydantic V2

    QA: Pytest (Suite asíncrona)

🏗️ Estructura del Proyecto
Plaintext

sgf_backend/
│
├── app/
│   ├── api/            # Capa de red (Routers y Dependencias)
│   │   ├── endpoints/  # Controladores (infracciones, auth, evidencias)
│   │   └── deps.py     # Dependencias (DB, Auth, Bypass)
│   ├── core/           # Configuración (settings, database, security)
│   ├── models/         # Modelos SQLAlchemy (DB)
│   ├── repositories/   # Capa de datos (Lógica de persistencia)
│   ├── schemas/        # Contratos de datos (Pydantic)
│   ├── services/       # Lógica de negocio y utilidades (Archivos, hash)
│   ├── tests/          # Suite de pruebas (pytest)
│   └── main.py         # Punto de entrada de FastAPI
│
├── storage/            # Almacenamiento local de evidencias
├── alembic/            # Migraciones de base de datos
├── .env                # Variables de entorno (No subir a Git)
├── iniciar_sistema.bat # Script de arranque (Doble clic)
└── requirements.txt    # Dependencias

🛠️ Instalación Local

    Clonar el repositorio:
    Bash

    git clone <url-de-tu-repo>
    cd sgf_backend

    Entorno Virtual:
    Bash

    python -m venv venv
    venv\Scripts\activate

    Instalar dependencias:
    Bash

    pip install -r requirements.txt

    Configurar variables:
    Crea un archivo .env en la raíz basado en los ejemplos, configurando DATABASE_URL, SECRET_KEY, y DEBUG=True.

    Migrar Base de Datos:
    Bash

    alembic upgrade head

🏃‍♂️ Ejecución

Para iniciar el sistema de forma profesional (sin abrir consola manualmente):

    Doble clic en el archivo: iniciar_sistema.bat

        Este script activará el entorno, lanzará el servidor y abrirá automáticamente la documentación en http://127.0.0.1:8000/docs.

🧪 Pruebas Automatizadas

Para validar que la API mantiene su integridad y resiliencia ante fallos:
Bash

pytest -v

(Se recomienda ejecutar esto tras cualquier cambio en el repositorio o la lógica de negocio).
🔐 Desarrollo y Seguridad

    Bypass de Desarrollo: Para pruebas con Flutter sin login, utiliza el token dev-flutter-token-123 en el header Authorization: Bearer dev-flutter-token-123.

    Seguridad de Archivos: El backend utiliza validación de Magic Bytes para asegurar que solo se suban imágenes válidas, rechazando ejecutables camuflados.

Notas adicionales para el equipo municipal:

    Backup: Se recomienda respaldar periódicamente la carpeta storage/evidencias y realizar un pg_dump de la base de datos sgf_core.

    Logs: Los errores críticos se registran en la consola de ejecución y son persistentes en el log del sistema.