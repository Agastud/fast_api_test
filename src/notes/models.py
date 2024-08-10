from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeMeta, Mapped, declarative_base, mapped_column

metadata = sa.MetaData()


class BaseServiceModel:
    """Базовый класс для таблиц сервиса."""

    @classmethod
    def on_conflict_constraint(cls) -> tuple | None:
        return None


Base: DeclarativeMeta = declarative_base(metadata=metadata, cls=BaseServiceModel)


class NoteModel(Base):
    __tablename__ = 'note'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String())
    content: Mapped[str] = mapped_column(String())
    created_at: Mapped[datetime] = mapped_column(DateTime())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime())

    def __repr__(self) -> str:
        return f'User(id={self.id!r}, title={self.title!r}, content={self.content!r}), created_at={self.created_at!r}, updated_at={self.updated_at!r}'
