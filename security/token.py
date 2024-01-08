# -------------------------------- python imports --------------------------
import uuid
from datetime import datetime, timedelta

# -------------------------------- FastAPI imports --------------------------
from fastapi import   Request
from fastapi.security import OAuth2PasswordBearer

# -------------------------------- Package imports --------------------------
from jose import JWTError, jwt,ExpiredSignatureError

# -------------------------------- Settings imports --------------------------
from settings.config import settings
from settings.database import get_db_session_to_variable 

# -------------------------------- Security imports --------------------------
from security.exceptions import ( 
    TOKEN_EXPIRED_EXCEPTION, 
    INVALID_TOKEN_EXCEPTION,
    USER_DOES_NOT_EXIST_EXCEPTION,
    DELETED_USER_EXCEPTION
)

# -------------------------------- Exception imports --------------------------
from security.custom_exception import CustomException

# -------------------------------- models imports --------------------------
import models



async def create_access_token(
        user_id            : int, 
        email              : str, 
):
    """
       this function will create access token for given user_id & email
    """

    lifetime           =   timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    expire             =   datetime.utcnow() + lifetime
    payload            =   {
        "type"         :   "ACCESS_TOKEN",
        "exp"          :   expire,
        "iat"          :   datetime.utcnow(),
        "user_id"      :   str(user_id),
        "email"        :   email,
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)


async def decode_token(token: str):

    try:

        payload       =   jwt.decode(token, settings.JWT_SECRET, algorithms=settings.ALGORITHM)
        user_id       =   payload.get("user_id")
        db            =   get_db_session_to_variable()
            
        if not user_id:
            raise CustomException(*INVALID_TOKEN_EXCEPTION)
        
        
        user = db.query(models.User).get(user_id)
        db.close()
        
        if not user:
            raise CustomException(*USER_DOES_NOT_EXIST_EXCEPTION)
        
        if not user.is_active:
            raise CustomException(*DELETED_USER_EXCEPTION)
        
        if user.is_removed:
            raise CustomException(*DELETED_USER_EXCEPTION)
        
        return user
    
    except ExpiredSignatureError:
        raise CustomException(*TOKEN_EXPIRED_EXCEPTION)
        
    except JWTError:
        raise CustomException(*INVALID_TOKEN_EXCEPTION)
        
    