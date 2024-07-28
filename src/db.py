from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('postgres')


def get_session():
    with Session(engine) as session:
        yield session