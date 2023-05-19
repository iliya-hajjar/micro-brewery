import uuid
from utils.uid import UUID
from sqlalchemy.sql import func
import sqlalchemy.types as types
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text


Base = declarative_base()


@dataclass
class Order(Base):
    id: str
    transaction_id: str
    user_id: str
    created_at: str
    updated_at: str

    __tablename__ = 'order_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(Integer)
    user_id = Column(Integer)
    created_at = Column(DateTime(timezone=False), server_default=func.now())
    updated_at = Column(types.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())


@dataclass
class OrderDetails(Base):
    id: int
    order_id: str
    product_id: str
    created_at: str

    __tablename__ = 'order_details_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer)
    order_id = Column(Integer, ForeignKey(Order.id))
    order = relationship('Order', foreign_keys='OrderDetails.order_id')
    created_at = Column(DateTime(timezone=False), server_default=func.now())
