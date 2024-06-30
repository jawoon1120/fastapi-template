from datetime import datetime

from sqlalchemy import DateTime, Identity, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase,AsyncAttrs):
    pass

class BaseEntity(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Identity(start=1, increment=1), primary_key=True, sort_order=-1)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deleted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()