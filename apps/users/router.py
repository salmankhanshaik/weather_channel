# -------------------------------- FastAPI imports ---------------------------
from fastapi          import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

# -------------------------------- sqlalchemy imports -------------------------
from sqlalchemy.orm import Session

# --------------------------------- settings imports ---------------------------
from settings.database import get_db

# -------------------------------- security imports ----------------------------
from security import token

# ------------------------------------- global utils Enums ---------------------
from utils.schemas  import BaseResponseSchema

# ------------------------------------- global enums ----------------------------
from constants.enums import StatusType

# ---------------------------------- app imports --------------------------------
from apps.users import  schemas 
from apps.users import  service as user_services


# initializing a router for user app
user_router         =   APIRouter(
    prefix          =   "/users",
    tags            =   ["Account"]
)



@user_router.post(
    path            =   "/sign_up/", 
    summary         =   "Create new user", 
    status_code     =   status.HTTP_201_CREATED,
)
async def user_sign_up(
        request_schema  : schemas.UserSignInRequestSchema,
        db: Session = Depends(get_db)
):
    """
       Complete Registration process of User where password is hashed then save into db
    """
    
    # validating the request body, raise excecption if validation failed
    await user_services.validate_sign_up_user_details(request_schema)
    
    # validating if user email already exist if exist raise exception
    await user_services.validate_is_user_email_already_exists(
        user_email        =  request_schema.email,
        db                =  db
    )

    # creating the user 
    await user_services.create_user(
        user_data         =  request_schema,
        db                =  db 
    )
    
    # returning the response
    response              =  BaseResponseSchema(
        status            =  StatusType.SUCCESS.value,
        message           =  "User SignUp Successful",
    )    
    return response




@user_router.post(
    path              =  "/login/", 
    summary           =  "Login user", 
    status_code       =   status.HTTP_200_OK,
    response_model    =  schemas.UserLoginInResponseSchema
)
async def user_login(
        request_schema :  schemas.UserLoginInRequestSchema,
        db: Session    =  Depends(get_db)
):
    """
       this endpoint will take username ,password from request body then return access token
    """
    
    # validating if user email already exist if exist raise exception
    user_object        =  await user_services.validate_is_email_exists(
        email          =  request_schema.email,
         db            =  db
    )
    
    # creating the access token with the given details
    created_token      =   await token.create_access_token(
        user_id        =   user_object.id,
        email          =   user_object.email,
    )
    
    # check the password with given password
    await user_services.validate_is_user_password_correct(
        account_password = user_object.password,
        entered_password = request_schema.password
    )
    
    # returning the response with the created token
    response           =   schemas.UserLoginInResponseSchema(
        status         =   StatusType.SUCCESS.value,
        message        =   "User Login Successful",
        access_token   =   created_token
        
    )    
    return response




@user_router.post(
    path              =   "/login/swagger",
    summary           =   "Login user via swagger authorize button", 
    status_code       =   status.HTTP_200_OK,

)
async def user_login_swagger(
    request_schema    :   OAuth2PasswordRequestForm = Depends(),
    db                :   Session                   = Depends(get_db)
):
    """
       this endpoint will take username ,password from request body then return access token
    """
    
    request_schema     =   jsonable_encoder(request_schema)

    # validating if user email already exist if exist raise exception
    user_object        =   await user_services.validate_is_email_exists(
        email          =   request_schema["username"],
        db             =   db
    )
    
    # creating the access token with the given details
    created_token      =   await token.create_access_token(
        user_id        =   user_object.id,
        email          =   user_object.email,
    )
    
    # check the password with given password
    await user_services.validate_is_user_password_correct(
        account_password = user_object.password,
        entered_password = request_schema["password"]
    )
    

    return schemas.UserLoginSwaggerResponse(
        access_token   =    created_token, 
        email          =    request_schema["username"]
    )