# --------------------------------- python imports ---------------------
import requests
from   datetime import date

# --------------------------------- sqlachemy imports -------------------
from sqlalchemy.orm import Session

# --------------------------------- settings imports ---------------------
from settings.config import settings

# --------------------------------- global Exception imports -------------
from security.custom_exception import CustomException

# ---------------------------------- models imports-------------------------------
import models

# ---------------------------------- utitls imports -------------------------------
from utils.viewsets import create_factory_method

# --------------------------------- app imports --------------------------
from apps.weather import exceptions


    

async def weather_api(
    location       : str,
    forecast_days  : int
):
    """
       it will get the weather information for given location by making 
       a api call to weather_api 
       if information found return it else return not found message
    """
    try:
        if forecast_days:        
            base_url    =  settings.WEATHER_API_BASE_URL + "forecast.json"
        else:
            base_url    =  settings.WEATHER_API_BASE_URL + "current.json"
        
        # complete url address by appending api_key & location 
        url        =  base_url + "?key=" + settings.WEATHER_API_KEY + "&q=" + location

        # if forecast_days is given then append it to the url
        if forecast_days:
            url    =  url + f"&days={forecast_days}"

        # making a api call to get weather information of given location
        response   =  requests.get(url)
        
        # converting the response into json object
        response   =   response.json()

        if response.get("error"):
            raise CustomException(*exceptions.WEATHER_INFORMATION_NOT_EXISTS_EXCEPTION) 

        return response
    
    except Exception as error:
        #print(error)
        raise CustomException(*exceptions.SOMETHING_WENT_WRONG_EXCEPTION) 
        
	

async def check_forecast_range(forecast_days:int):
    """_
        it will check the forecast range b/w a range else raise a exception 
    """
    if not forecast_days <= 1 and forecast_days >= 3:
        raise CustomException(*exceptions.FORECAST_RANGE_EXCEPTION) 
    

async def location_validation(location:str):
    """
       it will check if given location contain any numberic values if yes raise a exception
    """
    if any(each_letter.isdigit() for each_letter in location):
        raise CustomException(*exceptions.LOCATION_NUMERIC_EXCEPTION) 
    

async def check_location_already_saved(
    location : str,
    user_id  : int,
    db       : Session
):
    """
       it will check if given location already saved for requested user if yes raise a exception
    """
    
    user_saved_location_object                  =  db.query(models.UserLocation).filter(
        models.UserLocation.location_name ==  location,
        models.UserLocation.user_id       ==  user_id
    ).first()
        
    if user_saved_location_object:
        raise CustomException(*exceptions.LOCATION_ALREADY_EXIST_EXCEPTION)
    


async def check_ratelimit(
    user_id  : int,
    db       : Session
):
    """
       it will check ratelimit count for given user if api_hit_count is exceed then raise a exception
    """
    # getting the current date
    today    = date.today()
    
    # checking if user requested the server today
    user_rate_limit_object                   =   db.query(models.UserRateLimit).filter(
        models.UserRateLimit.requested_date ==   today,
        models.UserRateLimit.user_id        ==   user_id
    ).first()
    
    # if user requested today then check the ratelimit 
    if user_rate_limit_object:
        if not user_rate_limit_object.api_hit_count < settings.API_RATE_LIMIT:
            raise CustomException(*exceptions.QUOTA_EXCEEDED_EXCEPTION)


async def create_or_update_user_rate_limit_object(
    user_id  : int,
    db       : Session
):
    """
       it will check ratelimit count for given user if api_hit_count is exceed then raise a exception
    """
    # getting the current date
    today    = date.today()
    
    # checking if user requested the server today
    user_rate_limit_object                   =   db.query(models.UserRateLimit).filter(
        models.UserRateLimit.requested_date ==   today,
        models.UserRateLimit.user_id        ==   user_id
    ).first()
    
    # if user requested today then update the ratelimit 
    if user_rate_limit_object:
        user_rate_limit_object.api_hit_count +=  1
        db.commit()
    
    else:
        # schema required to create userratelimit object
        create_schema = {
            "requested_date"  :  today,
            "api_hit_count"   :  1,
            "user_id"         :  user_id,
        } 

        # creating a new user with given details raise exception if failed to create
        await create_factory_method(
            model_name        =  models.UserRateLimit,
            request_schema    =  create_schema,
            db                =  db
        )
            

async def get_user_location_weather_information(
    user_id : int,
    db      : Session
):
    """
       it will return the user saved location weather information
    """
    try:
        
        # checking if saved location found for given user_id
        user_location_objects             =  db.query(models.UserLocation).filter(
            models.UserLocation.user_id  ==  user_id,
        ).with_entities(models.UserLocation.location_name).all()

        # if saved location found then make a api call to weather_api & format location with its weather information
        if user_location_objects:
            
            # formating the locations
            locations                       = [each[0] for each in user_location_objects]
            weather_informations            = []

            # iterating over each location and getting the weather information
            for location in locations:
                
                # making a weather_api call to get the location's weather_information
                response = await weather_api(location=location,forecast_days=None)

                # if weather information available then add it to the list
                if response:
                    
                    response['current']['location'] = location
                    
                    # appending each location with weather api response
                    weather_informations.append(response['current'])
            else:
                print(weather_informations)
                return weather_informations   
    
    except Exception as e:
        return False   