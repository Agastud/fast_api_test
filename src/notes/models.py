from datetime import datetime

import sqlalchemy as sa
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
    title: Mapped[str] = mapped_column(sa.String())
    content: Mapped[str] = mapped_column(sa.String())
    created_at: Mapped[datetime] = mapped_column(sa.DateTime(), default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(sa.DateTime())

    def __repr__(self) -> str:
        return f'User(id={self.id}, ' f'title={self.title}, ' f'content={self.content}), ' f'created_at={self.created_at}, ' f'updated_at={self.updated_at}'
