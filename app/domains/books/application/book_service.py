from typing import Annotated
from fastapi import Depends

from app.domains.books.infra.book_entity import BookEntity
from ..infra.book_repostiory import BookRepository


class BookService:
    def __init__(self, book_repository = Depends(BookRepository)):
        self.book_repoistory = book_repository
    
    async def get_books(self) -> list[BookEntity]:
        
        books = await self.book_repoistory.get_books()
        return books