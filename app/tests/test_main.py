import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker
from httpx import AsyncClient

from app.common.infra.base import Base
from app.core.database.async_session import get_db_session
from app.main import app
from app.configs.app_config import get_postgres_test_connection

TEST_DATABASE_URL = get_postgres_test_connection()

test_engine = create_async_engine(TEST_DATABASE_URL)
TestingSessionLocal = async_sessionmaker(bind=test_engine, expire_on_commit=False)


# Override the get_db dependency
async def override_get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with TestingSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise

app.dependency_overrides[get_db_session] = override_get_db_session

@pytest.fixture(scope="module")
async def client() -> AsyncGenerator[AsyncClient, None]:
    # Create the database tables
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

    # Drop the database tables after the tests
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.anyio
async def test_read_root(client: AsyncClient):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Add more test cases as needed
