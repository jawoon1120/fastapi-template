
from typing import Annotated
from fastapi import APIRouter, Depends

from app.domains.users.application.user_service import UserService
from app.domains.users.presentation.dto.create_user_req import CreateUserRequestDTO


router = APIRouter(tags=["user"])

@router.post(
    "/users"
)
async def create_user(
    user_service : Annotated[UserService, Depends(UserService)],
    body: CreateUserRequestDTO
):
    await user_service.create_user(email=body.email, password=body.password)