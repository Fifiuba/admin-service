from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Admin(Base):
    __tablename__ = "administrators"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(255))
    last_name = Column("last_name", String(255), nullable=False)
    email = Column("email", String(255), nullable=False)
    token_id = Column("token_id", String(255), nullable=True)
