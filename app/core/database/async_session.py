from ...configs.app_config import get_postgres_connection
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

engine = create_async_engine(get_postgres_connection())
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    
    factory = async_sessionmaker(engine)
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
