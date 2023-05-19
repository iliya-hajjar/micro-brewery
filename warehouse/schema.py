import uuid
from sqlalchemy.sql import func
import sqlalchemy.types as types
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text


Base = declarative_base()


@dataclass
class Category(Base):
    id: int
    name: str
    create_at: str

    __tablename__ = 'category_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)
    create_at = Column(DateTime(timezone=False), server_default=func.now())


@dataclass
class Supplier(Base):
    id: str
    name: str
    address: str
    category_id: int
    create_at: str

    __tablename__ = 'supplier_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)
    address = Column(Text(300), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id))
    category = relationship('Category', foreign_keys='Supplier.category_id')
    create_at = Column(DateTime(timezone=True), server_default=func.now())


@dataclass
class Product(Base):
    id: str
    name: str
    price: float
    brand: str
    count: int
    location: str
    description: str
    supplier_id: str
    category_id: int
    create_at: str
    updated_at: str

    __tablename__ = 'product_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(FLOAT, nullable=False)
    brand = Column(String(100), nullable=False)
    count = Column(Integer, nullable=False)
    location = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)

    supplier_id = Column(Integer, ForeignKey(Supplier.id))
    supplier = relationship('Supplier', foreign_keys='Product.supplier_id')

    category_id = Column(Integer, ForeignKey(Category.id))
    category = relationship('Category', foreign_keys='Product.category_id')

    create_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(types.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
