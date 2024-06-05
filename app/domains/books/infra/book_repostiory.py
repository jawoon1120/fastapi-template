from sqlalchemy import select

from fastapi import Depends
from app.common.infra.repository import Repository
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database.async_session import get_db_session
from app.domains.books.infra.book_entity import BookEntity


class BookRepository(Repository):
    def __init__(self, session:AsyncSession = Depends(get_db_session)):
        super().__init__(session = session)

    async def get_books(self):
        query = select(BookEntity)
        result = await self.session.execute(query)
        return result.scalars().all()