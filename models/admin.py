# -------------------------------- Packages imports ---------------------------
from sqladmin             import ModelView

# -------------------------------- Project Files imports ---------------------------
from models.user_models   import User,UserLocation,UserRateLimit


class UserLocationAdmin(ModelView, model=UserLocation):
    column_list            = [UserLocation.location_name,UserLocation.user] 

class UserRateLimitAdmin(ModelView, model=UserRateLimit):
    column_list            = [UserRateLimit.api_hit_count,UserRateLimit.requested_date] 

class UserAdmin(ModelView, model=User):
    column_list            = [User.first_name,User.email]
