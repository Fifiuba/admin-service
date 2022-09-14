from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()



if "RUN_ENV" in os.environ.keys() and os.environ["RUN_ENV"] == "test":
    # read from .env file, if DATABASE_URL does not exist
    # then read from system env
    DB_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
else:
    DB_URL = os.getenv("DATABASE_URL")

# an Engine, which the Session will use for connection
# resources
engine = create_engine(
    DB_URL, echo=True
)
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
