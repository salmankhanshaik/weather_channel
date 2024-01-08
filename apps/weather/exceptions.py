from fastapi import status
from constants.enums import StatusType


WEATHER_INFORMATION_NOT_EXISTS_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "weather information for given location not found"
)


SOMETHING_WENT_WRONG_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "server is not responding please try later"
)


FORECAST_RANGE_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "we are only supporting weather forecast for next 3 days starting counting from today So please enter no of day b/w 1 to 3"
)

LOCATION_NUMERIC_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "location should not contains any numeric value"
)

LOCATION_ALREADY_EXIST_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "location already exit please save a new location"
)


QUOTA_EXCEEDED_EXCEPTION = (
    status.HTTP_400_BAD_REQUEST,
    StatusType.ERROR.value,
    "quota exceeded for today, you have reached daily limit of 5 requests per day"
)