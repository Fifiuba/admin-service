from fastapi import APIRouter, status, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from typing import List
from admin_service.database import admin_repository, schemas, database
from admin_service.security import jwt_handler, authorization, firebase
from admin_service.errors import exceptions

admin_route = APIRouter()


@admin_route.get(
    "/",
    response_model=List[schemas.AdminResponse],
    status_code=status.HTTP_200_OK,
)
async def get_admins(req: Request, db: Session = Depends(database.get_db)):
    try:
        authorization.is_auth(req.headers)
    except exceptions.AdminUnauthorized as error:
        raise HTTPException(**error.__dict__)
    else:
        admins = admin_repository.get_admins(db)
        return admins


@admin_route.get(
    "/{id}",
    response_model=schemas.AdminResponse,
    status_code=status.HTTP_200_OK,
)
async def get_admin(id: int, req: Request, db: Session = Depends(database.get_db)):

    try:
        authorization.is_auth(req.headers)
        admin = admin_repository.get_admin_by_id(id, db)
    except exceptions.AdminNotFoundError as error:
        raise HTTPException(**error.__dict__)
    except exceptions.AdminUnauthorized as error:
        raise HTTPException(**error.__dict__)
    else:
        return admin


@admin_route.get(
    "/my/profile",
    response_model=schemas.AdminResponse,
    status_code=status.HTTP_200_OK,
)
async def me(req: Request, db: Session = Depends(database.get_db)):
    try:
        authorization.is_auth(req.headers)
        token = authorization.get_token(req.headers)
    except exceptions.AdminUnauthorized as error:
        raise HTTPException(**error.__dict__)
    else:
        token_id = jwt_handler.decode_token(token)["id"]
        admin = admin_repository.get_admin_by_id(token_id, db)
        return admin


@admin_route.post(
    "/",
    response_model=schemas.AdminResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_admin(
    admin: schemas.AdminRequest,
    req: Request,
    db: Session = Depends(database.get_db),
    firebase=Depends(firebase.get_fb),
):
    try:
        authorization.is_auth(req.headers)
        uid = firebase.create_admin(admin.email, admin.password)
        admin_response = admin_repository.create_admin(admin, uid, db)
    except exceptions.AdminAlreadyExists as error:
        raise HTTPException(**error.__dict__)
    except exceptions.AdminUnauthorized as error:
        raise HTTPException(**error.__dict__)
    else:
        return admin_response


@admin_route.post(
    "/login",
    response_model=schemas.TokenResponse,
    status_code=status.HTTP_200_OK,
)
async def login_admin(
    admin: schemas.LoginAdminRequest, db: Session = Depends(database.get_db)
):
    try:
        email, uid = firebase.valid_admin(admin)
        admin_response = admin_repository.auth(email, uid, db)
        token = jwt_handler.create_access_token(admin_response.id, True)
        token_data = schemas.TokenResponse(token=token)
    except exceptions.AdminBadCredentials as error:
        raise HTTPException(**error.__dict__)

    return token_data
