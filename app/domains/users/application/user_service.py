from __future__ import annotations
from fastapi import Depends
from typing import TYPE_CHECKING

from app.domains.users.infra.user_entity import UserEntity
from app.domains.users.infra.user_repository import UserRepository

if TYPE_CHECKING:
    from app.domains.auth.application.auth_service import AuthService

class UserService:
    def __init__(
        self, 
        user_repository: UserRepository = Depends(UserRepository),
        auth_service: 'AuthService' = Depends('AuthService'),
    ):
        self.user_repository:UserRepository = user_repository
        self.auth_servcie:'AuthService' = auth_service

    async def _get_user_or_none(self, email:str) -> UserEntity | None:
        user: UserEntity | None = await self.user_repository.get_user_or_none(email = email)

        return user

    async def create_user(self, email:str, password:str):

        hashed_password = self.auth_servcie._get_password_hash(password)
        user = await self.user_repository.create_user(email=email, password=hashed_password)
        
        await user