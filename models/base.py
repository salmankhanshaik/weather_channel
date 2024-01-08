# -------------------------------- Python imports ---------------------------
import uuid


# -------------------------------- Packages imports ---------------------------
from sqlalchemy.sql import func
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer
)
from sqlalchemy.orm import declarative_base, declarative_mixin, declared_attr


# ----- intialize the base -------
Base = declarative_base()


@declarative_mixin
class BaseMixin:
    __abstract__ = True

    id              =   Column(Integer, primary_key=True)
    is_deleted      =   Column(Boolean, server_default='f') # for record delete
    created_at      =   Column(DateTime(timezone=True), server_default=func.now())
    updated_at      =   Column(DateTime(timezone=True), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        given_table_name = cls.__name__
        converted_table_name = ''.join(
            ['_' + char.lower() if char.isupper() else char for char in given_table_name]
        ).lstrip('_')
        converted_table_name += 's'
        return converted_table_name
