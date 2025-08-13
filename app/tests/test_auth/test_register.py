import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app

class TestRegisterUser:
    @pytest.fixture
    def valid_user_data(self):
        return {
            "username": "testuser122",
            "password": "testpassword123",
        }

    @pytest.fixture
    def invalid_user_data(self):
        return {
            "username": "",
            "password": "123",
        }

    @pytest.fixture
    def unicode_user_data(self):
        return {
            "username": "тестовыйюзер",
            "password": "пароль123",
        }

    @pytest.mark.asyncio
    async def test_register_success(self, valid_user_data):
        async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
            response = await client.post("auth/register/", json=valid_user_data)

            assert response.status_code == 200
            response_json = response.json()
            assert response_json["message"] == "OK"

    @pytest.mark.asyncio
    async def test_register_failure(self, invalid_user_data):
        async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
            response = await client.post("auth/register/", json=invalid_user_data)

            assert response.status_code == 422
            response_json = response.json()

    @pytest.mark.asyncio
    async def test_registration_with_existing_username(self, valid_user_data):
        async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
            response = await client.post("auth/register/", json=valid_user_data)

            assert response.status_code == 400
            response_json = response.json()
            assert response_json["detail"] == "User already exist"

    @pytest.mark.asyncio
    async def test_registration_with_unicode(self, unicode_user_data):
        async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
            response = await client.post("auth/register/", json=unicode_user_data)

            assert response.status_code == 422
            response_json = response.json()

