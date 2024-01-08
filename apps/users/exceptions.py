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

INCORRECT_OLD_PASSWORD = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Old password is not correct"
)

NEW_PASSWORD_SAME_AS_OLD_PASSWORD = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "New Password should not be same as old password"
)

INVALID_PASSWORD_LENGTH_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Password length must be {} or more"
)


INVALID_NUMBER_LENGTH_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Number length must be {}"
)


NUMBER_SHOULD_BE_NUMERIC = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "Number should not contain any characters"
)

