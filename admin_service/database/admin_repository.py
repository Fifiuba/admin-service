from . import schemas, crud
from admin_service.errors import exceptions
from sqlalchemy.orm import Session


def get_admins(db: Session):
    query_response = crud.get_admins(db)
    return query_response


def get_admin_by_id(id: int, db: Session):
    query_response = crud.get_admin(id, db)
    if not query_response:
        raise exceptions.AdminNotFoundError
    return query_response


def auth(email: str, uid: str, db: Session):
    admin = crud.get_admins_by_email(email, db)
    if not admin:
        raise exceptions.AdminBadCredentials
    if not uid == admin.token_id:
        raise exceptions.AdminBadCredentials

    return admin


def create_admin(admin: schemas.AdminRequest, uid: str, db: Session):
    admin_response = crud.create_admin(admin, uid, db)
    return admin_response


def find_by_username(user_name: str, db: Session):
    return crud.get_admins_by_user_name(user_name, db)


def update_admin(admin_id: int, admin: schemas.AdminUpdateRequest, db: Session):
    admin_updated = crud.update(admin_id, admin, db)
    return admin_updated


def delete_admin(admin_id, firebase, db: Session):
    admin = crud.get_admin(admin_id, db)
    firebase.delete_admin(admin.token_id)
    id = crud.delete_admin(admin.id, db)
    return id
