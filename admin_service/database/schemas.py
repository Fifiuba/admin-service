from typing import List
from pydantic import BaseModel


class AdminRequest(BaseModel):
    name: str
    last_name: str
    user_name: str
    password: str


class AdminResponse(BaseModel):
    id: int
    name: str
    last_name: str
    user_name: str
    password: str

    class Config:
        orm_mode = True


class TokenResponse(BaseModel):
    token: str
