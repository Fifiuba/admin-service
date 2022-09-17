from . import database, models, schemas, crud
from typing import List
from sqlalchemy.orm import Session


def get_admins(db: Session):
    query_response = crud.get_admins(db)
    return query_response


def create_admin(admin: schemas.AdminRequest, db: Session):

    admin_response = crud.create_admin(admin, db)
    return admin_response
