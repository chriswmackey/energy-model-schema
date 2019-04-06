from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models.database import Base
from app.core.config import DATABASE_URL

from starlette.exceptions import HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

try:
    engine = create_engine(str(DATABASE_URL))
except AttributeError:
    raise HTTPException(
        HTTP_500_INTERNAL_SERVER_ERROR,
        detail='Failed to initialize database')

# create session
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> Session:
    """create a new session and return for each request."""
    db_session = LocalSession()
    return db_session
