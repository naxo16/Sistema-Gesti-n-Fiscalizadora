# Context Engineering: Backend DERA (Desarrollo, Ejecución y Reglas de API)

## Alcance MVP
Debido a los estrictos límites de tiempo, el desarrollo de esta fase se centra EXCLUSIVAMENTE en:
- El módulo de **infracciones vehiculares**.
- La operación y sincronización de arquitectura **Offline-First**.

## Endpoints Permitidos
La API para este MVP está estrictamente limitada a los siguientes endpoints (No crear otros):

1. **`POST /api/v1/auth/login`**
   - **Propósito:** Autenticación de inspectores y emisión del token JWT.

2. **`POST /api/v1/infracciones/sync`**
   - **Propósito:** Endpoint crítico para la operación Offline-First. 
   - **Comportamiento:** Recibe un JSON plano masivo desde la aplicación móvil (Drift SQLite). Utiliza SQLAlchemy de forma asíncrona para desarmar el payload e insertarlo transaccionalmente en `registros_base`, `infracciones_vehiculares` y `evidencias_fotograficas`.

3. **`GET /api/v1/infracciones`**
   - **Propósito:** Listar los resultados de las infracciones sincronizadas.
