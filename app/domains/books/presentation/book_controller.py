from typing import Annotated
from fastapi import APIRouter, Depends, status

from app.domains.auth.infra.auth_required import AuthRequired

from ..application.book_service import BookService
from ..presentation.dto.get_books_res import EnquiryDetail

router = APIRouter(tags=["book"])

@router.get(
    "/books", 
    response_model=list[EnquiryDetail], 
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(AuthRequired())]
)
async def get_books(
    book_service : Annotated[BookService, Depends(BookService)]
):
    res = await book_service.get_books()

    return res

@router.post(
    "/books", 
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(AuthRequired())]
)
async def create_books_with_transaction(
    book_service : Annotated[BookService, Depends(BookService)]
):
    res = await book_service.create_book_one_two()

    return res


