import asyncio
from fastapi.testclient import TestClient
from models import Admin


def test_create_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):  # nosec
    response = client.post("/api/v1/admin", json={"username": "test", "password": "test"})
    assert response.status_code == 200
    assert "test" in response.text
    user_id = response.json()["data"]["id"]

    async def get_user_by_db():
        user = await Admin.get(id=user_id)
        return user

    user_obj = event_loop.run_until_complete(get_user_by_db())
    assert user_obj.id == user_id
