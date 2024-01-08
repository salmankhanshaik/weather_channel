# -------------------------------- Sqlachemy imports -----------------------
from    pydantic           import   BaseModel
from    typing             import   Union, Dict,List


# -------------------------------- constants imports -------------------------
from    constants.enums    import   StatusType


class BaseResponseSchema(BaseModel):
    status             : StatusType
    message            : str
    data               : Union[Dict, None] = None

    class Config:
        orm_mode = True
