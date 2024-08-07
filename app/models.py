from sqlalchemy import Column,Integer, String

from .database import Base

#table for phones
class Phone(Base):
    __tablename__ = "phones" #table name

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    brand = Column(String)
    color = Column(String)
    price = Column(String)
    quantity = Column(Integer)
    description = Column(String)


#tables for users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

