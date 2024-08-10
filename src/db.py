from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres')


def get_session() -> Generator:
    with Session(engine) as session:
        yield session
