from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from admin_service.database import admin_repository, schemas, database
from admin_service.security import password_hasher

admin_route = APIRouter()


@admin_route.get(
    "/",
    response_model=List[schemas.AdminResponse],
    status_code=status.HTTP_200_OK,
)
async def get_admins(db: Session = Depends(database.get_db)):

    admins = admin_repository.get_admins(db)

    return admins


@admin_route.post(
    "/",
    response_model=schemas.AdminResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_admin(
    admin: schemas.AdminRequest, db: Session = Depends(database.get_db)
):
    admin.password = password_hasher.hash_password(admin.password)
    admin_response = admin_repository.create_admin(admin, db)
    return admin_response
