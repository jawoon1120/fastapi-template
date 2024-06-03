from typing import Annotated
from fastapi import APIRouter, Depends, status

from ..application.book_service import BookService
from ..presentation.dto.get_books_res import EnquiryDetail

router = APIRouter(tags=["book"])

@router.get(
    "/books", 
    response_model=list[EnquiryDetail], 
    status_code=status.HTTP_200_OK
)
def get_books(
    book_service : Annotated[BookService, Depends(BookService)]
):
    res = book_service.get_books()

    return res
