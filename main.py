
# -------------------------------- packages imports ---------------------------
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# -------------------------------- fastapi imports -----------------------------
from fastapi                    import FastAPI,Request
from fastapi.middleware.cors    import CORSMiddleware
from fastapi.testclient         import TestClient
from fastapi.templating         import Jinja2Templates
from fastapi.staticfiles        import StaticFiles

# -------------------------------- packages imports -----------------------------
from sqladmin import Admin

# -------------------------------  settings imports ------------------------------
from settings.config           import settings
from settings.database         import engine

# -------------------------------  security imports ------------------------------
from security.custom_exception import CustomException

# -------------------------------- admin imports ----------------------------------
from models.admin              import UserAdmin,UserLocationAdmin,UserRateLimitAdmin


# ------------------------------- app router imports --------------------------------
from apps.users.router        import user_router
from apps.weather.router      import weather_router
from apps.weather.cron_mail   import send_weather_information_mail


# ------------------------------- fast_api default configuration --------------------
app                                 =     FastAPI(
    swagger_ui_parameters           =    {"operationsSorter": "method", "tagsSorter": "alpha"},
    redoc_url                       =    settings.REDOCS_URL,
    swagger_ui_oauth2_redirect_url  =    f"/{settings.DOCS_URL}/oauth2-redirect",
 )


# -------------------------- custom exception configuration  --------------------------
@app.exception_handler(CustomException)
async def unicorn_exception_handler(request: Request, exc: CustomException):
    """
    It will catch the custom exceptions that are raised and returns a Json response in given format
    status: [SUCCESS, ERROR]
    message: str
    data: {} or None
    """
    from starlette.responses import JSONResponse

    return JSONResponse(
        status_code  = exc.status_code,
        content      = {"status": exc.custom_status, "message": exc.message, "data": exc.data},
)

# -------------------------- middle_ware configuration  -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------- router configuration  -------------------------------------
app.include_router(prefix="/api",router=user_router)
app.include_router(prefix="/api",router=weather_router)

# -------------------------- static configuration  -------------------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")


# -------------------------- admin configuration  ---------------------------------------
admin = Admin(app, engine,base_url=settings.ADMIN_URL)
admin.add_view(UserAdmin)
admin.add_view(UserLocationAdmin)
admin.add_view(UserRateLimitAdmin)


# ---------------------------- app startup  -----------------------------------------------
@app.on_event('startup')
async def init_data():
    
    # creating a instance of background scheduler
    scheduler          =  BackgroundScheduler()
    
    # adding a cron job to the scheduler
    scheduler.add_job(
        send_weather_information_mail, 
        'cron',
        minute         =  settings.WEATHER_MAIL_CRON_JOB_MINUTE,
        hour           =  settings.WEATHER_MAIL_CRON_JOB_HOUR,
        day            =  '*',
        month          =  '*',
        day_of_week    =  '*',
    )
    
    # starting the schedular when app starts
    print("Schedular starts at",datetime.datetime.now())
    scheduler.start()