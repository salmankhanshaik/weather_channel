# --------------------------------- sqlachemy imports ------------------------
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

# --------------------------------- global exception imports ----------------
from security.custom_exception import CustomException

# ---------------------------------- Models ---------------------------------
import models

# --------------------------------- global utilts imports --------------------
from utils.viewsets import create_factory_method

# --------------------------------- constants imports ------------------------
from constants import plain_constants

# --------------------------------- app imports ------------------------------
from apps.users import exceptions
from apps.users import utils





async def validate_sign_up_user_details(user_data):
    """ 
       it will validate the user sign Up Details raise exception if validation fails
    """
    
    # raise Exception if first_name minimum length is not satisfied
    if len(user_data.first_name) < plain_constants.MINIMUM_FIRST_NAME_LENGTH:
        custom_message      = list(exceptions.INVALID_FIRST_NAME_LENGTH_EXCEPTION)
        custom_message[2]   = custom_message[2].format(plain_constants.MINIMUM_FIRST_NAME_LENGTH)
        raise CustomException(*custom_message)

    # raise Exception if last_name minimum length is not satisfied
    if len(user_data.last_name) < plain_constants.MINIMUM_LAST_NAME_LENGTH:
        custom_message      = list(exceptions.INVALID_LAST_NAME_LENGTH_EXCEPTION)
        custom_message[2]   = custom_message[2].format(plain_constants.MINIMUM_LAST_NAME_LENGTH)
        raise CustomException(*custom_message)

    # raise Exception if password minimum length is not satisfied
    if len(user_data.password) < plain_constants.MINIMUM_PASSWORD_LENGTH:
        custom_message      = list(exceptions.INVALID_PASSWORD_LENGTH_EXCEPTION)
        custom_message[2]   = custom_message[2].format(plain_constants.MINIMUM_PASSWORD_LENGTH)
        raise CustomException(*custom_message)

    # raise Exception if email is not valid
    if not utils.is_valid_email(email=user_data.email):
        raise CustomException(*exceptions.INVALID_EMAIL_EXCEPTION)
    


async def validate_is_user_email_already_exists(db: Session, user_email: str,third_party:bool=False):
    """
       it will check if user provided email already exist in the system
       raise exception if email already Exist
    """
    email = db.query(models.User).filter(models.User.email == user_email).first()
        
    if email:
        raise CustomException(*exceptions.EMAIL_ALREADY_EXISTS_EXCEPTION)     
    
    

async def create_user(user_data:dict,db: Session):
    """
        creating the user in the system with required information
    """
    # hashing the password
    hashed_password       =  utils.hash_password(user_data.password)

    # user_model request schema
    create_user_object_request_schema = {
        "first_name"      :  user_data.first_name,
        "last_name"       :  user_data.last_name,
        "email"           :  user_data.email,
        "password"        :  hashed_password,
        "date_joined"     :  func.now(),
    } 
        
    # creating a new user with given details raise exception if failed to create
    await create_factory_method(
        model_name        =  models.User,
        request_schema    =  create_user_object_request_schema,
        db                =  db
    )
    

async def validate_is_email_exists(email: str,db: Session):
    """
       It will check if user provided email already exist in the system
       raise Exception if email already Exist
    """
    
    # check for valid email
    if not utils.is_valid_email(email):
        raise CustomException(*exceptions.EMAIL_IS_NOT_VALID_EXCEPTION) 
        
    user_object = db.query(models.User).filter(models.User.email == email).first()

    if user_object is None:
        raise CustomException(*exceptions.EMAIL_NOT_EXISTS_EXCEPTION) 
    
    return user_object


async def validate_is_user_password_correct(account_password:str,entered_password: str):
    if not utils.verify_password(hashed_password=account_password,plain_password=entered_password):
        raise CustomException(*exceptions.PASSWORD_INCORRECT_EXCEPTION) 
