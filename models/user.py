from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from config.db import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)