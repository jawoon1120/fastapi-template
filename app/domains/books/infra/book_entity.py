from app.common.infra.base import BaseEntity
from sqlalchemy.orm import Mapped, mapped_column

class BookEntity(BaseEntity):
    __tablename__ = "book"

    name: Mapped[str] = mapped_column()
    author: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
