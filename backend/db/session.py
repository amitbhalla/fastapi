from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings

SQLALCHEMY_DATABSE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABSE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
