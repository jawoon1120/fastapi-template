from fastapi import Depends, HTTPException

from app.domains.users.infra.user_entity import UserEntity
from app.domains.users.infra.user_repository import UserRepository

class UserService:
    def __init__(
        self, 
        user_repository : UserRepository = Depends(UserRepository),
    ):
        self.user_repository :UserRepository = user_repository
    
    async def get_user_or_none(self, email:str) -> UserEntity | None:
        user: UserEntity | None = await self.user_repository.get_user_or_none(email = email)

        return user

    async def create_user(self, email:str, hashed_password:str) -> UserEntity:
        existed_user = await self.get_user_or_none(email=email)
        if existed_user:
            raise HTTPException(status_code=409, detail="중복 유저가 존재합니다")
        
        user = await self.user_repository.create_user(email=email, password=hashed_password)

        return user