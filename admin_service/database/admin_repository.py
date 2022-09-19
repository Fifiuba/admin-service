from . import database, models, schemas, crud
from typing import List
from sqlalchemy.orm import Session


def get_admins(db: Session):
    query_response = crud.get_admins(db)
    return query_response

def get_admin_by_id(id:int ,db:Session):
    query_response = crud.get_admin(id,db)
    return query_response


def create_admin(admin: schemas.AdminRequest, db: Session):

    admin_response = crud.create_admin(admin, db)
    return admin_response

def find_by_username(user_name:str, db: Session):
    return crud.get_admins_by_user_name(user_name, db)