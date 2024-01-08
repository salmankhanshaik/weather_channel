# -------------------------------- packages imports ---------------------------
import asyncio

# -------------------------------  settings imports ---------------------------
from settings.config           import settings
from settings.database         import get_db_session_to_variable

# -------------------------------- email  imports -----------------------------
from email_services.smtp       import smtp_service

# -------------------------------- email  imports -----------------------------
import models

# --------------------------------- app imports --------------------------------
from apps.weather              import service as weather_services 


def send_weather_information_mail():
    """it will send a weather informatin mail to user saved location"""
    
    print("=========================cron_mail================================")
    
    # creating a database session
    db             =  get_db_session_to_variable()
    
    # getting all the active users 
    user_objects   =  db.query(models.User).filter(
        models.User.is_deleted == False
    ).all()
    
    # iterating over each user and sending a weather mail
    for user_object in user_objects:
    
        # getting all the user saved location weather information
        location_weather_informations  =  asyncio.run(
            weather_services.get_user_location_weather_information(
                user_id                =  user_object.id,
                db                     =  get_db_session_to_variable()
            )
        )

        # sending mail for location_weather_informations exist
        if location_weather_informations:
        
            asyncio.run(
                smtp_service.send_weather_information_mail(
                    email                          =   user_object.email, 
                    name                           =   user_object.first_name + user_object.last_name,
                    location_weather_informations  =   location_weather_informations
                )
            )
