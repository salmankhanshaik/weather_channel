# -------------------------------- Python imports ---------------------------
import pathlib


# -------------------------------- FastAPI imports ---------------------------
from pydantic     import    BaseSettings
from fastapi_mail import ConnectionConfig


# project directories
ROOT = pathlib.Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    
    # --------- token --------------
    JWT_SECRET                 : str   
    ALGORITHM                  : str   
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    # --------- urls ---------------   
    DOCS_URL                   : str
    REDOCS_URL                 : str
    ADMIN_URL                  : str
    DATABASE_URL               : str
    TOKEN_URL                  : str
    BASE_URL                   : str
    
    # ----- weather api ------------
    WEATHER_API_BASE_URL       : str
    WEATHER_API_KEY            : str
    
    # ----- rate limit  ------------
    API_RATE_LIMIT             : int
    
    # ------ mail information -------
    MAIL_USERNAME              : str          
    MAIL_PASSWORD              : str
    MAIL_FROM                  : str
    MAIL_PORT                  : int
    MAIL_SERVER                : str
    MAIL_TLS                   : bool
    MAIL_SSL                   : bool
    USE_CREDENTIALS            : bool
    TEMPLATE_FOLDER            : str
    
    # ------- mail sync -------------
    WEATHER_MAIL_CRON_JOB_MINUTE : str
    WEATHER_MAIL_CRON_JOB_HOUR   : str
    
    class Config:
        case_sensitive = True
        env_file       = ".env"


settings = Settings()


conf = ConnectionConfig(
    MAIL_USERNAME      =    settings.MAIL_USERNAME,
    MAIL_PASSWORD      =    settings.MAIL_PASSWORD,
    MAIL_FROM          =    settings.MAIL_FROM,
    MAIL_PORT          =    settings.MAIL_PORT,
    MAIL_SERVER        =    settings.MAIL_SERVER,
    MAIL_TLS           =    settings.MAIL_TLS,
    MAIL_SSL           =    settings.MAIL_SSL,
    USE_CREDENTIALS    =    settings.USE_CREDENTIALS,
    TEMPLATE_FOLDER    =    settings.TEMPLATE_FOLDER,
)


