# Weather Channel
--  Get Historical Weather Data, Real-Time Weather Information & Accurate Weather Forecasts.
--  SignUp Now and Check Weather for your City (Daily 5 requests For Free)
--  Save your Favorite Location and Daily Weather Updates to your Email for Free !!!


# Folder Structure 

Project Structure/
└── weather_channel/
    ├── apps/
    │   ├── users/            ---   User Management Endpoints
    │   │   ├── service.py    ---   Logic Methods
    │   │   ├── schemas.py    ---   Request and Response Schemas
    │   │   ├── router.py     ---   Endpoint Defintion
    │   │   ├── exception.py  ---   App Level Exceptions
    │   │   ├── test_.py      ---   App Level Test Cases
    │   │   └── utils.py      ---   App Level Helpers 
    │   └── weather
    ├── constants/            ---   Project Level Constants     
    ├── email_services/       ---   Email Functionality  
    ├── migrations/           ---   Model Migration Files
    ├── models/               ---   Model Definition
    ├── security/             ---   Project Level Security
    ├── settings/             ---   Project Level Settings
    ├── static/               ---   Project Level Templates
    ├── utils/                ---   Project Level Helpers
    └── main.py               ---   Entry Point


# Create a Virtual Environment 
    
    ----------------------------------------------
    | python3 -m venv <name_of_your_environment> |
    ----------------------------------------------

#  Activate the Virtual Environment 
#  Install  all the Dependencies

    ----------------------------------------------
    | python3 install -r requirements.py         |
    ----------------------------------------------
    
#  Run the server

    ----------------------------------------------
    | uvicorn main:app --reload                  |
    ----------------------------------------------

#  Create a PostgreSQL Database

    ----------------------------------------------
    | CREATE DATABASE <your_database_name>       |
    ----------------------------------------------

#  Migrate the changes

    ----------------------------------------------
    | alembic upgrade head                       |
    ----------------------------------------------



