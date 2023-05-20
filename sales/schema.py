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
    transaction_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=False), server_default=func.now())
    updated_at = Column(types.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    def to_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


@dataclass
class OrderDetails(Base):
    id: int
    order_id: str
    product_id: str
    product_count: int
    created_at: str

    __tablename__ = 'order_details_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_count = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    order_id = Column(Integer, ForeignKey(Order.id), nullable=False)
    order = relationship('Order', foreign_keys='OrderDetails.order_id')
    created_at = Column(DateTime(timezone=False), server_default=func.now())

    def to_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
