# ---------------------------- fastapi imports  ------------------------------------------
from fastapi         import status

# ---------------------------- app imports  -----------------------------------------------
from test_apps       import client

# ---------------------------- settings imports  ------------------------------------------
from settings.config import settings

# ---------------------------- constants imports  -----------------------------------------
from constants       import enums

# ---------------------------- app startup  -----------------------------------------------
from apps.weather    import exceptions


        
def test_weather_without_authentication():
    """
        this will test the weather endpoint without bearer token
    """     
    url                          =   settings.BASE_URL + "/api/weather/"
    
    # making a api call and comparing the status code
    response                     =   client.get(url=url)
    assert response.status_code ==   status.HTTP_401_UNAUTHORIZED


def get_access_token():
    """
        this will return the access token
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
    response                   =   response.json()
    
    # returning the access token
    assert response["status"]  ==  enums.StatusType.SUCCESS
    return response["access_token"]
    

def test_weather_with_invalid_query_paramter():
    """
        this will test the weather endpoint without invalid query paramter 
    """     
    location                       =   "london123"
    url                            =   settings.BASE_URL + "/api/weather/" + "?location=" + location
    
    # getting the access token
    access_token                   =   get_access_token()
    
    # making a api call and converting the response into json
    response                       =   client.get(
        url                        =   url,
        headers = {
            'Authorization'        :  'Bearer {}'.format(access_token)
       }
    )

    # converting the response into json and checking the response with status
    response                       =   response.json()
    assert response["status"]      ==  enums.StatusType.ERROR
    assert response["message"]     ==  exceptions.LOCATION_NUMERIC_EXCEPTION[2]
    
    

def test_weather_with_authentication():
    """
        this will test the weather endpoint without bearer token
    """     
    location                       =   "london"
    url                            =   settings.BASE_URL + "/api/weather/" + "?location=" + location
    
    # getting the access token
    access_token                   =   get_access_token()
    
    # making a api call and converting the response into json
    response                       =   client.get(
        url                        =   url,
        headers = {
            'Authorization'        :  'Bearer {}'.format(access_token)
       }
    )
    
    # checking for valid response
    if response.status_code        ==   status.HTTP_200_OK:
        
        # converting the response into json and checking the response with status
        response                   =    response.json()
        assert response["status"]  ==   enums.StatusType.SUCCESS

    # checking for invalid response
    elif response.status_code      ==   status.HTTP_400_BAD_REQUEST:
        
        # converting the response into json and checking the response with status.message
        response                   =    response.json()
        assert response["status"]  ==   enums.StatusType.ERROR
        assert response["message"] ==   exceptions.SOMETHING_WENT_WRONG_EXCEPTION[2]    
