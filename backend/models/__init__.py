from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Binary

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    username = Column(String)
    password = Column(String)
    email = Column(String, primary_key=True)
    phone = Column(String)
    picture = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)
    fname = Column(String)
    lname = Column(String)
    num_transactions = Column(String)
    rating = Column(Integer)

    def __init__(self):
        username = ''

    def __str__(self):
        return f'{self.fname} {self.lname}'

# class idk
