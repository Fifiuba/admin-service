from . import database,models,schemas,crud
from typing import List
from sqlalchemy.orm import Session

def get_admins(db: Session):
    query_response = crud.get_admins(db)
    print(query_response)
    return query_response

