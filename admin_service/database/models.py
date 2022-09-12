from sqlalchemy.orm import declarative_base
from database import engine

Base = declarative_base()


class Admin(Base):
    __table__ = "administrators"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    username = Column(String)
    password = Column(String)


Base.metadata.create_all(engine)
