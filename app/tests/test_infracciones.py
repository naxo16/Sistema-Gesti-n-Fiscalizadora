# app/tests/test_infracciones.py
import pytest
from httpx import AsyncClient
import uuid
from datetime import datetime, timezone

from app.main import app
from app.api.deps import get_dispositivo_actual, get_db

# --- MOCKS (Simuladores de Dependencias) ---

async def mock_get_dispositivo_actual():
    """Simula una sesión stateless válida de un dispositivo en terreno"""
    return "imei_hash_test_123s"

class MockFailingSession:
    """Simulador de una conexión de SQLAlchemy que colapsa en el momento de la verdad"""
    async def execute(self, *args, **kwargs):
        raise Exception("Critical: Connection timeout to PostgreSQL cluster on 5432")

async def mock_get_db_con_falla():
    """Inyecta el caballo de Troya al Router"""
    yield MockFailingSession()

# --- UTILIDAD: Payload Base Válido ---
def generar_payload_valido():
    return {
        "id": str(uuid.uuid4()),
        "dispositivo_id": str(uuid.uuid4()),
        "tipo": "VEHICULO",
        "fecha_emision": datetime.now(timezone.utc).isoformat(),
        "ubicacion": {"lat": -33.4569, "lng": -70.6482},
        "vehiculo": {
            "patente": "AB1234",
            "marca_modelo": "Toyota Yaris",
            "color": "Gris"
        }
    }

# --- CASOS DE PRUEBA DE RESILIENCIA ---

async def test_sync_sin_token_rechaza_401(client: AsyncClient):
    """
    SGI-IT-01: Dispositivo sin token o expirado.
    Debe responder 401 para que el móvil detenga la cola y pida re-autenticación.
    """
    app.dependency_overrides = {} # Limpiamos overrides previos
    payload = generar_payload_valido()
    
    response = await client.post("/api/v1/infracciones/sync", json=payload)
    
    assert response.status_code == 401

async def test_sync_payload_corrupto_rechaza_422(client: AsyncClient):
    """
    SGI-UT-01: Datos corruptos desde terreno (Falta ubicación).
    Debe responder 422 para que el móvil marque el registro como inválido y NO reintente.
    """
    app.dependency_overrides[get_dispositivo_actual] = mock_get_dispositivo_actual
    
    payload_invalido = generar_payload_valido()
    del payload_invalido["ubicacion"] # Forzamos corrupción quitando un campo obligatorio
    
    response = await client.post("/api/v1/infracciones/sync", json=payload_invalido)
    
    assert response.status_code == 422
    assert "ubicacion" in response.text
    
    app.dependency_overrides = {}

async def test_sync_falla_servidor_gatilla_backoff_500(client: AsyncClient):
    """
    SGI-IT-02: Error sistémico interno (BD inalcanzable).
    Debe responder 500 estructurado para gatillar el Backoff Exponencial en Flutter.
    """
    # Forzamos la autenticación exitosa pero destruimos la conexión a la base de datos
    app.dependency_overrides[get_dispositivo_actual] = mock_get_dispositivo_actual
    app.dependency_overrides[get_db] = mock_get_db_con_falla
    
    payload = generar_payload_valido()
    response = await client.post("/api/v1/infracciones/sync", json=payload)
    
    assert response.status_code == 500
    assert "Exponential Backoff" in response.json()["detail"]
    
    # IMPORTANTE: Limpiar los overrides al finalizar para no alterar otros tests
    app.dependency_overrides = {}