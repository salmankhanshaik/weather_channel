# ---------------------------- fastapi imports  ------------------------------------------
from fastapi         import status

# ---------------------------- app imports  -----------------------------------------------
from test_apps       import client

# ---------------------------- settings imports  ------------------------------------------
from settings.config import settings

# ---------------------------- constants imports  -----------------------------------------
from constants       import plain_constants
from constants       import enums

# ---------------------------- app startup  -----------------------------------------------
from apps.users      import exceptions


        
def test_create_user_first_name_field():
    """
        this will test the user creation endpoint with following cases
        1) first_name length must be 3 or more
    """
    # sample payload to test the first_name 
    sample_payload             =  {
        "first_name"           :  "sa",
        "last_name"            :  "khan",
        "email"                :  "salman_khan@example.com",
        "password"             :  "salman_khan@123"
    }
    
    # making a api call and converting the response into json
    response                   =   client.post(
        url                    =   f"{settings.BASE_URL}/api/users/sign_up/", 
        json                   =   sample_payload
    )
    response                   =   response.json()
    
    # getting the first_name exception message & formatting with constants
    custom_message             =   list(exceptions.INVALID_FIRST_NAME_LENGTH_EXCEPTION)
    custom_message[2]          =   custom_message[2].format(plain_constants.MINIMUM_FIRST_NAME_LENGTH)
    
    # checking the response with status,error message
    assert response["status"]  ==  enums.StatusType.ERROR
    assert response["message"] ==  custom_message[2]


def test_create_user_last_name_field():
    """
        this will test the user creation endpoint with following cases
        1) last_name  length must be 3 or more
         
    """
    # sample payload to test the last_name 
    sample_payload             =  {
        "first_name"           :  "salman",
        "last_name"            :  "kh",
        "email"                :  "salman_khan@example.com",
        "password"             :  "salman_khan@123"
    }
    
    # making a api call and converting the response into json
    response                   =   client.post(
        url                    =   f"{settings.BASE_URL}/api/users/sign_up/", 
        json                   =   sample_payload
    )
    response                   =   response.json()
    
    # getting the first_name exception message & formatting with constants
    custom_message             =   list(exceptions.INVALID_LAST_NAME_LENGTH_EXCEPTION)
    custom_message[2]          =   custom_message[2].format(plain_constants.MINIMUM_LAST_NAME_LENGTH)
    
    # checking the response with status,error message
    assert response["status"]  ==  enums.StatusType.ERROR
    assert response["message"] ==  custom_message[2]
    

def test_create_user_password_field():
    """
        this will test the user creation endpoint with following cases
        1) password  length must be 3 or more
         
    """
    # sample payload to test the password 
    sample_payload             =  {
        "first_name"           :  "salman",
        "last_name"            :  "khan",
        "email"                :  "salman_khan@example.com",
        "password"             :  "salman"
    }
    
    # making a api call and converting the response into json
    response                   =   client.post(
        url                    =   f"{settings.BASE_URL}/api/users/sign_up/", 
        json                   =   sample_payload
    )
    response                   =   response.json()
    
    # getting the first_name exception message & formatting with constants
    custom_message             =   list(exceptions.INVALID_PASSWORD_LENGTH_EXCEPTION)
    custom_message[2]          =   custom_message[2].format(plain_constants.MINIMUM_PASSWORD_LENGTH)
    
    # checking the response with status,error message
    assert response["status"]  ==  enums.StatusType.ERROR
    assert response["message"] ==  custom_message[2]
    
    
def test_create_user():
    """
        this will test the user creation endpoint
        if user doesn't exist then create & test the flow
        if user already exist then test the flow for signup again
    """
    # sample payload to test the entire user creation flow 
    sample_payload             =  {
        "first_name"           :  "salman",
        "last_name"            :  "khan",
        "email"                :  "salman.khan@example.com",
        "password"             :  "salman@123"
    }
    
    # making a api call 
    response                   =   client.post(
        url                    =   f"{settings.BASE_URL}/api/users/sign_up/", 
        json                   =   sample_payload
    )
    
    # checking for user created test case and also user trying to sign up again test case
    if response.status_code        ==  status.HTTP_201_CREATED:
        
        # converting the response into json and checking the response with status
        response                   =   response.json()
        assert response["status"]  ==  enums.StatusType.SUCCESS
    
    elif response.status_code      ==  status.HTTP_400_BAD_REQUEST:
        
        # converting the response into json and checking the response with message
        response                   =   response.json()
        assert response["message"] ==  exceptions.EMAIL_ALREADY_EXISTS_EXCEPTION[2]
    

def test_login_user_with_valid_credentials():
    """
        this will test the user login endpoint with correct credentials
    """
    # sample payload to test the login 
    sample_payload             =  {
        "email"                :  "salman.khan@example.com",
        "password"             :  "salman@123"
    }
    # making a api call 
    response                   =   client.post(
        url                    =   f"{settings.BASE_URL}/api/users/login/", 
        json                   =   sample_payload
    )
    
    assert response.status_code == status.HTTP_200_OK


def test_login_user_with_wrong_password():
    """
        this will test the user login endpoint with correct credentials
    """
    # sample payload to test the login 
    sample_payload             =  {
        "email"                :  "salman.khan@example.com",
        "password"             :  "salman@12"
    }
    # making a api call 
    response                   =   client.post(
        url                    =   f"{settings.BASE_URL}/api/users/login/", 
        json                   =   sample_payload
    )
    response                   =   response.json()
    assert response["message"] ==  exceptions.PASSWORD_INCORRECT_EXCEPTION[2]