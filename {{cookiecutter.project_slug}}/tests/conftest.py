import asyncio

import pytest
from app.core.config import settings
from app.main import app
from httpx import AsyncClient


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_client():
    async with AsyncClient(app=app, base_url=f"http://test{settings.API_V1_STR}") as ac:
        yield ac
