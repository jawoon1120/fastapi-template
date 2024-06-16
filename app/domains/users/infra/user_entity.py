from app.common.infra.base import BaseEntity
from sqlalchemy.orm import Mapped, mapped_column

class UserEntity(BaseEntity):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
