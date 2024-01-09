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
    DELETED_USER_EXCEPTION,
)

# -------------------------------- Exception imports --------------------------
from  security.custom_exception import CustomException

# -------------------------------- models imports --------------------------
import models




class OAuth2PasswordBearerCustom(OAuth2PasswordBearer):
    def __init__(self, token_url):
        super(OAuth2PasswordBearerCustom, self).__init__(tokenUrl=token_url)

    async def __call__(self, request: Request):
        res               =   await super().__call__(request)
        res               =   res.replace('Bearer', '')
        res               =   res.replace(' ', '')
        try:
            payload       =   jwt.decode(res, settings.JWT_SECRET, algorithms=settings.ALGORITHM)
            user_id       =   payload.get("user_id")
            db            =   get_db_session_to_variable()
            
            if not user_id:
                raise CustomException(*INVALID_TOKEN_EXCEPTION)

            user = None
            
            try:
                user = db.query(models.User).get(user_id)
            
            except Exception:
                raise CustomException(*INVALID_TOKEN_EXCEPTION)

            db.close()

            if not user:
                raise CustomException(*USER_DOES_NOT_EXIST_EXCEPTION)
        
            if user.is_deleted:
                raise CustomException(*DELETED_USER_EXCEPTION)

            # appending user data to request state
            request.state.user    = user
            return user

        except ExpiredSignatureError:
            raise CustomException(*TOKEN_EXPIRED_EXCEPTION)
        
        except JWTError:
            raise CustomException(*INVALID_TOKEN_EXCEPTION)


    
oauth2_scheme        = OAuth2PasswordBearerCustom(token_url=settings.TOKEN_URL)