from sqlalchemy.orm import Session

from . import models, schemas


def get_admin(admin_id: int, db: Session):
    return db.query(models.Admin).filter(models.Admin.id == admin_id).first()


def get_admins_by_name(name: str, db: Session):
    return db.query(models.Admin).filter(models.Admin.name == name).all()


def get_admins(db: Session):
    return db.query(models.Admin).all()


def create_admin(admin: schemas.AdminRequest, db: Session):
    db_admin = models.Admin(
        name = admin.name,
        last_name = admin.last_name,
        user_name = admin.user_name,
        password= admin.password,
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin