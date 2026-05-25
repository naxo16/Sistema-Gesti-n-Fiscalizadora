# app/tests/conftest.py
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.fixture
async def client() -> AsyncClient:
    """
    Cliente de pruebas asíncrono de FastAPI.
    El transport ASGITransport procesa las peticiones en memoria sin levantar sockets reales.
    """
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://testserver"
    ) as ac:
        yield ac