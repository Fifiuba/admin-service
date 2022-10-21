# flake8: noqa

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from .models import Base

load_dotenv()


def init_database():
    DB_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DB_URL, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_local_session():
    return SessionLocal()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
