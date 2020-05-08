from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Binary

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    userid = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    username = Column(String)
    password = Column(Binary)
    email = Column(String)

    def __str__(self):
        return f'{self.fname} {self.lname}: {self.username}, {self.password}'

# class idk
