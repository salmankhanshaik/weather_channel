# ------------------------ package imports -------------------------------------
from pydantic            import EmailStr
from fastapi_mail        import MessageSchema, FastMail

# ------------------------- settings imports -------------------------------------
from settings.config import conf as fastapi_email_config

# ------------------------- security imports -------------------------------------
from security.custom_exception import CustomException


async def send_weather_information_mail(
    email                           :    EmailStr, 
    name                            :    str,
    location_weather_informations   :    list,
):
    message               =    MessageSchema(
        subject           =   "Weather Information",
        recipients        =    [email],  # List of recipients, as many as you can pass '
        template_body     =    {
            "first_name"          :    name,
            "location_weather_informations" :    location_weather_informations
        })
    
    fm                  =   FastMail(fastapi_email_config)
    await fm.send_message(message=message, template_name="weather_information.html")
    