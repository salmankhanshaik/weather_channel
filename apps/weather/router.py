# -------------------------------- FastAPI imports ---------------------------
from fastapi    import APIRouter, Depends, status,Request

# -------------------------------- sqlalchemy imports ---------------------------
from sqlalchemy.orm import Session

# --------------------------------- Settings imports ---------------------------
from settings.database import get_db
from security.authentication import oauth2_scheme

# -------------------------------- models imports --------------------------------
import models

# -------------------------------- global utils imports --------------------------
from utils.schemas  import BaseResponseSchema
from utils.viewsets import create_factory_method

# ------------------------------------- Global Enums ----------------------------
from constants.enums import StatusType

# ---------------------------------- App  imports ---------------------------
from apps.weather import  schemas 
from apps.weather import  service as weather_services


# initializing a router for weather app
weather_router         =   APIRouter(
    tags               =   ["Weather"],
    dependencies       =   [Depends(oauth2_scheme)]
)



@weather_router.get(
    path                =   "/weather/", 
    status_code         =   status.HTTP_201_CREATED,
    response_model      =   BaseResponseSchema
)
async def get_location_weather(
    request             :   Request,
    location            :   str,
    forecast_days       :   int = None,
    db: Session         =   Depends(get_db)
):
    """
       it will return weather information for given location
    """

    # getting the logged in user 
    requested_user_id    =  request.state.user.id
    
    # check for ratelimit for requested_user
    await weather_services.check_ratelimit(
        user_id          =  requested_user_id,
        db               =  db
    )
    
    # checking validation for forecast range
    if forecast_days:
        await weather_services.check_forecast_range(forecast_days=forecast_days)
    
    # checking validation for location
    await weather_services.location_validation(location=location)
    
    # validating the request body, raise excecption if validation failed
    weather_information   =   await weather_services.weather_api(
        location          =   location,
        forecast_days     =   forecast_days
    )
    
    # updating the ratelimit
    await weather_services.create_or_update_user_rate_limit_object(
        user_id           =   requested_user_id,
        db                =   db
    )
    
    # returning the response
    response              =   BaseResponseSchema(
        status            =   StatusType.SUCCESS.value,
        message           =   f"weather information found for the {location} location fetched successfully",
        data              =    weather_information
    )    
    return response



@weather_router.post(
    path                   =  "/users/location/", 
    status_code            =   status.HTTP_200_OK,
    response_model         =   BaseResponseSchema
)
async def create_user_location(
    request                :   Request,
    request_schema         :   schemas.UserLocationRequestSchema,
    db: Session            =   Depends(get_db)
):
    """
       this will save user entered location into db
    """
    
    # getting the logged in user 
    requested_user_id      = request.state.user.id
    
    # checking validation for location
    await weather_services.location_validation(location=request_schema.location)
    
    # checking if location already exit in db
    await weather_services.check_location_already_saved(
        location            =  request_schema.location,
        user_id             =  requested_user_id,
        db                  =  db
    )

    # creating schema for user_saved_location
    create_schema = {
        "user_id"           :  requested_user_id,
        "location_name"     :  request_schema.location 
    }
    
    # creating a new user with given details raise exception if failed to create
    await create_factory_method(
        model_name          =  models.UserLocation,
        request_schema      =  create_schema,
        db                  =  db
    )
    
    # returning the response
    response                =  BaseResponseSchema(
        status              =  StatusType.SUCCESS.value,
        message             =  f"given location {request_schema.location} saved successfully",
    )    
    return response
    
    