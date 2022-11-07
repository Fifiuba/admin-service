import os
from dotenv import load_dotenv

# from datetime import datetime, timedelta
from jose import jwt


load_dotenv()

if "RUN_ENV" in os.environ.keys() and os.environ["RUN_ENV"] == "test":
    JWT_SECRET_KEY = "testcase"
    ALGORITHM = "HS256"
else:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = 2

"""
    JWT Token type
    {
        "id": admin_id
        "admin":true
        "exp": 7 days
    }

"""


def create_access_token(admin_id: int, admin: str) -> str:
    # expires_delta: datetime = datetime.utcnow() + timedelta(
    #    minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"id": admin_id, "admin": admin}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def decode_token(token):
    payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
    return payload
