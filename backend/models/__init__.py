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


class Request(Base):
    __tablename__ = 'requests'

    requestID = Column(String, primary_key=True)
    user_email = Column(String, ForeignKey('users.email'))
    min_quantity = Column(Float)
    quantity = Column(Float)
    urgency = Column(Integer)
    item = Column(String)
    fulfilled = Column(Binary)

    def __init__(self, requestID, user_email, quantity, item, min_quantity, urgency=0):
        self.requestID = requestID
        self.user_email = user_email
        self.min_quantity = min_quantity
        self.quantity = quantity
        self.item = item
        self.urgency = urgency

    def __str__(self):
        return f'Request #{self.requestID} from {self.user_email}'

    def json(self):
        return {'request': {'requestID': self.requestID,
                            'user_email': self.user_email,
                            'min_quantity': self.min_quantity,
                            'quantity': self.quantity,
                            'item': self.item,
                            'urgency': self.urgency}}

