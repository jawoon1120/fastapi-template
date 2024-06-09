from typing import Annotated
from fastapi import Depends

from app.core.database.async_session import get_db_session
from app.domains.books.infra.book_entity import BookEntity
from ..infra.book_repostiory import BookRepository
from sqlalchemy.ext.asyncio import AsyncSession

class BookService:
    def __init__(
        self, 
        book_repository = Depends(BookRepository),
        session:AsyncSession = Depends(get_db_session)
    ):
        self.book_repoistory:BookRepository = book_repository
        self.session:AsyncSession = session

    async def get_books(self) -> list[BookEntity]:
        
        books = await self.book_repoistory.get_books()
        return books
    

    async def create_book_one_two(self):
        async with self.session.begin():
            self.book_repoistory.create_book_one()
            self.book_repoistory.create_book_two()
        # return