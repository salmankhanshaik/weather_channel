
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from settings.config import settings


engine         =  create_engine(settings.DATABASE_URL)
SessionLocal   =  sessionmaker(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        

def get_db_session_to_variable(autocommit=False):
    """
    This function will return a db_session
    that session should be closed manually
    :param schema:
    :return:
    """
    SessionLocal =  sessionmaker(bind=engine, autocommit=autocommit, autoflush=False, expire_on_commit=False)
    db           =  SessionLocal()
    return db