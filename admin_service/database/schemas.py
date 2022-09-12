from typing import List, Union
from pydantic import BaseModel


class AdminRequest(BaseModel):
    name: str
    last_name: str
    username: str
    password: str

class AdminResponse(BaseModel):
    id: int
    name: str
    last_name: str
    username: str
    password: str

    class Config:
        orm_mode: True
