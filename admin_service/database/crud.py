from sqlalchemy.orm import Session

from . import models, schemas
from admin_service.errors import exceptions


def get_admin(admin_id: int, db: Session):
    return db.query(models.Admin).filter(models.Admin.id == admin_id).first()


def get_admins_by_name(name: str, db: Session):
    return db.query(models.Admin).filter(models.Admin.name == name).all()


def get_admins_by_user_name(user_name: str, db: Session):
    return db.query(models.Admin).filter(models.Admin.user_name == user_name).first()


def get_admins(db: Session):
    return db.query(models.Admin).all()


def admin_exists(user_name: str, db: Session):
    q = get_admins_by_user_name(user_name, db)
    return True if q is not None else False


def create_admin(admin: schemas.AdminRequest, db: Session):
    if admin_exists(admin.user_name, db):
        raise exceptions.AdminAlreadyExists

    db_admin = models.Admin(
        name=admin.name,
        last_name=admin.last_name,
        user_name=admin.user_name,
        password=admin.password,
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin
