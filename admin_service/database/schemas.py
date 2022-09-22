from pydantic import BaseModel


class AdminRequest(BaseModel):
    name: str
    last_name: str
    email: str
    password: str


class AdminResponse(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    password: str
    token_id:str

    class Config:
        orm_mode = True


class LoginAdminRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    token: str
