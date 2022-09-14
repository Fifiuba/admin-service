import os
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

HASH = os.getenv("PASS_HASH")
password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def hash_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)