from fastapi import status
from constants.enums import StatusType



# ----------------------- For Sign Up --------------------------
INVALID_FIRST_NAME_LENGTH_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "First Name length must be {} or more"
)

INVALID_LAST_NAME_LENGTH_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Last Name length must be {} or more"
)

INVALID_PASSWORD_LENGTH_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Password length must be {} or more"
)

INVALID_EMAIL_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Invalid Email"
)

EMAIL_ALREADY_EXISTS_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Your email is already exists, please login to your account"
)

EMAIL_IS_NOT_VALID_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Your email is not valid "
)


PASSWORD_INCORRECT_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Your password is incorrect "
)

EMAIL_NOT_EXISTS_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "You are not registered with us, please Sign Up"
)


# --------------------------------- Password ------------------------------------
INVALID_PASSWORD_LENGTH_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Password length must be {} or more"
)
