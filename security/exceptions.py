from fastapi         import status
from constants.enums import StatusType


TOKEN_EXPIRED_EXCEPTION = (
    status.HTTP_401_UNAUTHORIZED,
    StatusType.ERROR.value,
    "Token is expired"
)

INVALID_TOKEN_EXCEPTION = (
    status.HTTP_401_UNAUTHORIZED,
    StatusType.ERROR.value,
    "Invalid Token"
)

USER_DOES_NOT_EXIST_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "User does Not Exists"
)

DELETED_USER_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "User deleted, please contact admin"
)
