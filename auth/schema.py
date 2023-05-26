from sqlalchemy.sql import func
import sqlalchemy.types as types
from dataclasses import dataclass
from sqlalchemy_utils import EmailType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String


Base = declarative_base()


@dataclass
class User(Base):
    id: str
    email: str
    password: str
    created_at: str
    updated_at: str

    __tablename__ = 'order_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(EmailType, unique=True)
    password = Column(String(50))
    created_at = Column(DateTime(timezone=False), server_default=func.now())
    updated_at = Column(types.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
