from pydantic       import   BaseModel, EmailStr
from typing         import   Optional
from utils.schemas  import   BaseResponseSchema


class UserSignInRequestSchema(BaseModel):
    """
       User SignIN Request Schema
    """
    first_name    : str
    last_name     : str
    email         : EmailStr
    password      : str
    

class UserSignInResponseSchema(BaseResponseSchema):
    """
       User SignIN Response Schema
    """
    pass


class UserLoginInRequestSchema(BaseModel):
    """
       User Login Request Schema
    """
    email      : str
    password   : str


class UserLoginInResponseSchema(BaseResponseSchema):
    """
       User Login Response Schema
    """
    access_token     :  str
    
    class Config:
        orm_mode = True  
        

class UserLoginSwaggerResponse(BaseModel):
    access_token : str
    email        : str