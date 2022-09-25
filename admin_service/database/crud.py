from sqlalchemy.orm import Session
from typing import Union
from . import models, schemas
from admin_service.errors import exceptions


def get_admin(admin_id: int, db: Session):
    return db.query(models.Admin).filter(models.Admin.id == admin_id).first()


def get_admins_by_name(name: str, db: Session):
    return db.query(models.Admin).filter(models.Admin.name == name).all()


def get_admins_by_email(email: str, db: Session):
    return db.query(models.Admin).filter(models.Admin.email == email).first()


def get_admins(db: Session):
    return db.query(models.Admin).all()


def admin_exists(email: str, db: Session):
    q = get_admins_by_email(email, db)
    return True if q is not None else False


def create_admin(admin: schemas.AdminRequest, token_id: Union[str, None], db: Session):
    if admin_exists(admin.email, db):
        raise exceptions.AdminAlreadyExists

    db_admin = models.Admin(
        name=admin.name,
        last_name=admin.last_name,
        email=admin.email,
        password=admin.password,
        token_id=token_id,
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def update(admin_id, admin: schemas.AdminUpdateRequest, db: Session):
    admin_found = get_admin(admin_id, db)

    if admin_found is None:
        raise exceptions.AdminNotFoundError

    setattr(admin_found, "name", admin.name)
    setattr(admin_found, "last_name", admin.last_name)

    db.commit()
    db.refresh(admin_found)

    return admin_found


def delete_admin(admin_id, db: Session):
    admin = get_admin(admin_id, db)
    id = admin.id
    db.delete(admin)
    db.commit()
    return id
