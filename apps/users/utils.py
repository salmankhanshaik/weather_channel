#-------------------------------- Python Imports -------------------
import re

#-------------------------------- Package Imports -------------------
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)   


def is_valid_email(email: str) -> bool:
    from constants.plain_constants import EMAIL_REGEX

    if re.fullmatch(EMAIL_REGEX, email):
        return True
    else:
        return False  
