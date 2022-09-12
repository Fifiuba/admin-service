from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import declarative_base
from .database import engine

Base = declarative_base()

class Admin(Base):
    __tablename__  = "administrators"

    id = Column("id",Integer, primary_key=True,autoincrement=True)
    name = Column("name",String(255))
    last_name = Column("last_name",String(255),nullable=False)
    user_name = Column("user_name", String(255), nullable=False)
    password = Column("password", String(255), nullable=False)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)