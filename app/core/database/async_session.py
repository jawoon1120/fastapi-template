from ...configs.app_config import get_postgres_connection
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
    async_scoped_session
)
import asyncio

engine = create_async_engine(get_postgres_connection())
session_factory = async_sessionmaker(bind=engine, autocommit=False, autoflush=True, expire_on_commit=False)

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:

    Session = async_scoped_session(session_factory, scopefunc=asyncio.current_task)

    async with Session() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await Session.remove()
            await engine.dispose()
