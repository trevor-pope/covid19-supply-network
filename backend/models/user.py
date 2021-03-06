from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Binary, Float

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
    num_transactions = Column(Integer)
    rating = Column(Integer)

    def __init__(self, username, password, email, phone='phone', picture='picture', street='street', city='city', state='state', zipcode='zipco', fname='fname', lname='lname', num_transactions=0, rating=5):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.picture = picture
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.fname = fname
        self.lname = lname
        self.num_transactions = num_transactions
        self.rating = rating

    def __str__(self):
        return f'{self.fname} {self.lname}: {self.username}'

    def json(self):
        return {'email': self.email,
                'phone': self.phone,
                'username': self.username,
                'picture': self.picture,
                'street': self.street,
                'city': self.city,
                'state': self.state,
                'zipcode': self.zipcode,
                'fname': self.fname,
                'lname': self.lname,
                'num_transactions': self.num_transactions,
                'rating': self.rating}
