from . import database, models, schemas, crud
from admin_service.errors import exceptions
from admin_service.security import password_hasher
from typing import List
from sqlalchemy.orm import Session


def get_admins(db: Session):
    query_response = crud.get_admins(db)
    return query_response

def get_admin_by_id(id:int ,db:Session):
    query_response = crud.get_admin(id,db)
    if not query_response:
        raise exceptions.AdminNotFoundError
    return query_response

def auth(user_name:str ,password:str ,db: Session):
    admin = crud.get_admins_by_user_name(user_name, db)
    if not admin:
        raise exceptions.AdminBadCredentials
    if not password_hasher.verify_password(password,admin.password):
        raise exceptions.AdminBadCredentials
    
    return admin


def create_admin(admin: schemas.AdminRequest, db: Session):
    admin_response = crud.create_admin(admin, db)
    return admin_response

def find_by_username(user_name:str, db: Session):
    return crud.get_admins_by_user_name(user_name, db)