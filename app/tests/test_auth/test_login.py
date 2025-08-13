import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app

@pytest.mark.asyncio
async def test_login_success(created_user):
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("auth/login/", json={"username": created_user["username"], "password": created_user["password"]})

        assert response.status_code == 200
        response_json = response.json()
        assert response_json["message"] == "OK"

@pytest.mark.asyncio
async def test_login_failure(created_user):
    invalid_user_data = {
        "username": "wronguser",
        "password": "wrongpassword"
    }
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("auth/login/", json=invalid_user_data)

        assert response.status_code == 404
        response_json = response.json()
        assert response_json["detail"] == "Username not found"

@pytest.mark.asyncio
async def test_login_wrong_password(created_user):
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("auth/login/", json={"username": created_user["username"], "password": "passwords1234"})

        assert response.status_code == 400
        response_json = response.json()
        assert "Incorrect password for username" in response_json["detail"]