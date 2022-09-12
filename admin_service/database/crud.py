from sqlalchemy.orm import Session

from . import models, schemas


def get_admin(admin_id: int, db: Session):
    return db.query(models.Admin).filter(models.Admin.id == admin_id).first()


def get_admins_by_name(name: str, db: Session):
    return db.query(models.Admin).filter(models.Admin.name == name).all()


def get_admins(db: Session):
    return db.query(models.Admin).all()
