import os
import pytest
from httpx import AsyncClient, ASGITransport
os.environ["MODE"]="TEST"
from app.config import settings
from app.database import async_session_maker, Base, engine
from app.main import app

@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

@pytest.fixture(scope="session")
async def db_session():
    async with async_session_maker() as session:
        yield session

@pytest.fixture(scope="session")
async def created_user():
    valid_user_data = {
        "username": "testuser12",
        "password": "testuser123"
    }
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("auth/register/", json=valid_user_data)
        assert response.status_code == 200
    yield valid_user_data


@pytest.fixture(scope="session")
async def authorized_user_empty():
    user_data = {
        "username": "testuser121",
        "password": "testuser121"
    }

    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        register_response = await client.post("auth/register/", json=user_data)
        assert register_response.status_code == 200

        user_info = register_response.json()
        user_id = user_info.get("user_id")

        response = await client.post("auth/login/", json={
            "username": user_data["username"],
            "password": user_data["password"]
        })
        assert response.status_code == 200
        assert response.cookies.get("access_token") is not None

        return {
            "access_token": response.cookies.get("access_token"),
            "username": user_data["username"],
            "id": user_id
        }


@pytest.fixture(scope="session")
async def authorized_user():
    user_data = {
        "username": "testtesttest",
        "password": "testtesttest"
    }

    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        register_response = await client.post("auth/register/", json=user_data)
        assert register_response.status_code == 200

        user_info = register_response.json()
        user_id = user_info.get("user_id")

        response = await client.post("auth/login/", json={
            "username": user_data["username"],
            "password": user_data["password"]
        })
        assert response.status_code == 200
        assert response.cookies.get("access_token") is not None

        return {
            "access_token": response.cookies.get("access_token"),
            "username": user_data["username"],
            "id": user_id
        }
