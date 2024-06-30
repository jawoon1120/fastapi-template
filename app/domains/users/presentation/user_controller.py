
from typing import Annotated
from fastapi import APIRouter, Depends

from app.domains.auth.application.auth_service import AuthService
from app.domains.users.application.user_service import UserService
from app.domains.users.presentation.dto.create_user_req import CreateUserRequestDTO
from app.domains.users.presentation.dto.create_user_res import CreateUserResponseDTO


router = APIRouter(tags=["user"])

@router.post(
    "/users",
    response_model=CreateUserResponseDTO
)
async def create_user(
    body: CreateUserRequestDTO,
    user_service : Annotated[UserService, Depends(UserService)],
    auth_seirvce : AuthService = Depends(AuthService),
):
    hashed_password = auth_seirvce.get_password_hash(password=body.password)
    user = await user_service.create_user(email=body.email, hashed_password=hashed_password)

    return CreateUserResponseDTO(id=user.id)
