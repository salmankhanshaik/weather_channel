from sqlalchemy import (
    TEXT,
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Date
)
from sqlalchemy.orm import relationship
from models.base    import Base, BaseMixin
from sqlalchemy.orm import relationship, backref



class User(Base,BaseMixin):
    """
        It Contains User Full Information
    """
    first_name              =    Column(String(25),  nullable=False)
    last_name               =    Column(String(25),  nullable=False)
    password                =    Column(String(256), unique=False, nullable=False)
    email                   =    Column(String(50), unique=False, nullable=True)
    date_joined             =    Column(DateTime(timezone=True), nullable=True)
    date_of_leaving         =    Column(DateTime(timezone=True), nullable=True)
    last_login_at           =    Column(DateTime(timezone=True))

    def __repr__(self):
       return f"{self.first_name} {self.last_name}"


class UserLocation(Base,BaseMixin):
    """
        it Contains User Full Information 
    """
    location_name           =    Column(TEXT,  nullable=False)
    user_id                 =    Column(Integer, ForeignKey(User.id, ondelete='CASCADE'), nullable=False)
    user                    =    relationship(User, backref=backref("users"))
    

class UserRateLimit(Base,BaseMixin):
    """
        it Contains User Full Information 
    """
    requested_date          =    Column(Date,  nullable=False)
    api_hit_count           =    Column(Integer,  nullable=False)
    user_id                 =    Column(Integer, ForeignKey(User.id, ondelete='CASCADE'), nullable=False)
    user                    =    relationship(User)