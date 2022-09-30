from pydantic import BaseModel


class AdminRequest(BaseModel):
    name: str
    last_name: str
    email: str
    password: str


class AdminUpdateRequest(BaseModel):
    name: str
    last_name: str


class AdminResponse(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    token_id: str

    class Config:
        orm_mode = True


class LoginAdminRequest(BaseModel):
    token: str


class LoginAdminResponse(BaseModel):
    name: str
    last_name: str
    token: str


class DeleteResponse(BaseModel):
    id: int
