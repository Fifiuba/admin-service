from fastapi import APIRouter, status, HTTPException,Depends
from admin_service.database import admin_repository, schemas,database
from sqlalchemy.orm import Session
from typing import List

admin_route = APIRouter()

@admin_route.get(
    "/admins",
    response_model=List[schemas.AdminResponse],
    status_code=status.HTTP_201_CREATED,
)
async def get_admins(db: Session = Depends(database.get_db)):
    
    admins = admin_repository.get_admins(db)

    return admins
