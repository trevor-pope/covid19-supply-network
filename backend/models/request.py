from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Binary, Float

Base = declarative_base()


class Request(Base):
    __tablename__ = 'requests'

    requestID = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String, ForeignKey('users.email'))
    min_quantity = Column(Float)
    quantity = Column(Float)
    urgency = Column(Integer)
    item = Column(String)

    def __init__(self, user_email, quantity, item, min_quantity, urgency=0):
        self.requestID = Request.requestID
        self.user_email = user_email
        self.min_quantity = min_quantity
        self.quantity = quantity
        self.item = item
        self.urgency = urgency

    # Note, we pull Request.requestID because we let it autoincrement,
    # but it only updates after the new request has been committed to the db, so we wary of that I guess. -Trevor
    def __str__(self):
        return f'Request {Request.requestID} from {self.user_email} (MAY NOT BE UNIQUE)'

    def json(self):
        return {'request': {'requestID': self.requestID,
                            'user_email': self.user_email,
                            'min_quantity': self.min_quantity,
                            'quantity': self.quantity,
                            'item': self.item,
                            'urgency': self.urgency}}

