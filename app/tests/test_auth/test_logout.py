import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app

@pytest.mark.asyncio
async def test_logout_success():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("auth/logout/")

        assert response.status_code == 200
        response_json = response.json()
        assert response_json["message"] == "OK"