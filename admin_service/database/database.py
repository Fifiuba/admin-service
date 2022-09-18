from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()


if "RUN_ENV" in os.environ.keys() and os.environ["RUN_ENV"] == "test":
    # read from .env file, if DATABASE_URL does not exist
    # then read from system env
    engine = create_engine(
        "sqlite:///./test.db", echo=True, connect_args={"check_same_thread": False}
    )
else:
    DB_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DB_URL, echo=True)


# an Engine, which the Session will use for connection
# resources

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_local_session():
    return SessionLocal()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
