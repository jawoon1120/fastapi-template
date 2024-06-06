import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from collections.abc import AsyncGenerator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker
from httpx import AsyncClient

from main import app, get_db_session
from configs.app_config import get_postgres_test_connection

TEST_DATABASE_URL = get_postgres_test_connection()

test_engine = create_async_engine(TEST_DATABASE_URL)
TestingSessionLocal = async_sessionmaker(bind=test_engine, expire_on_commit=False)

Base = declarative_base()

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
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

    # Drop the database tables after the tests
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_read_root(client: AsyncClient):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# Add more test cases as needed
