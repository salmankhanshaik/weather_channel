from pydantic       import   BaseModel, EmailStr
from typing         import   Optional
from utils.schemas  import   BaseResponseSchema


class UserLocationRequestSchema(BaseModel):
    """
       User Saved Location Request Schema
    """
    location    : str