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
    
    def create_book_one(self):
        book = BookEntity()
        book.name = "book_one"
        book.author = "jawoon_one"
        book.description = "good_one"
        self.session.add(book)
        

    def create_book_two(self):
        book = BookEntity()
        book.name = "book_two"
        book.author = "jawoon_two"
        book.description = "good_two"
        raise Exception({"detail":"error"})
        self.session.add(book)
        