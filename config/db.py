import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ.get("SQL_USER")}:{os.environ.get("SQL_PASSWORD")}@{os.environ.get("SQL_HOST")}:{os.environ.get("SQL_PORT")}/{os.environ.get("SQL_NAME")}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base