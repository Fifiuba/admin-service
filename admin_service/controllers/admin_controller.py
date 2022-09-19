from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from admin_service.database import admin_repository, schemas, database
from admin_service.security import password_hasher, jwt_handler

admin_route = APIRouter()


@admin_route.get(
    "/",
    response_model=List[schemas.AdminResponse],
    status_code=status.HTTP_200_OK,
)
async def get_admins(db: Session = Depends(database.get_db)):

    admins = admin_repository.get_admins(db)

    return admins

@admin_route.get(
    "/{id}",
    response_model=schemas.AdminResponse,
    status_code=status.HTTP_200_OK,
)
async def get_admins(id:int ,db: Session = Depends(database.get_db)):

    admin = admin_repository.get_admin_by_id(id,db)

    return admin


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

# TODO: Use Exceptions
@admin_route.post(
    "/login",
    response_model=schemas.TokenResponse,
    status_code=status.HTTP_200_OK,
)
async def create_admin(
    admin: schemas.LoginAdminRequest, db: Session = Depends(database.get_db)
):
    admin_response = admin_repository.find_by_username(admin.user_name, db)
    if password_hasher.verify_password(admin.password,admin_response.password):

        token = jwt_handler.create_access_token(admin_response.id, True)
        token_data = schemas.TokenResponse(token=token)
    else:
        token_data = schemas.TokenResponse(token='error')
    
    return token_data
