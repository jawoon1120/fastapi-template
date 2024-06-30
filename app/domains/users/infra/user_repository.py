from sqlalchemy import select

from fastapi import Depends
from app.common.infra.repository import Repository
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database.async_session import get_db_session
from app.domains.users.infra.user_entity import UserEntity


class UserRepository(Repository):
    def __init__(self, session:AsyncSession = Depends(get_db_session)):
        super().__init__(session = session)

    async def get_user_or_none(self, email:str) -> UserEntity | None:
        query = select(UserEntity).where(UserEntity.email == email)
        result = await self.session.execute(query)
        return result.scalars().one_or_none()

    async def create_user(self, email:str, password:str) -> UserEntity:
        user = UserEntity(
            email = email,
            password = password
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user