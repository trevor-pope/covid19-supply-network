from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Binary, Float

Base = declarative_base()

class Offer(Base):
    __tablename__ = 'requests'
    offerId = Column(Integer, primary_key=True, autoincrement=True)
    requestId = Column(Integer, ForeignKey('requests.requestId'))
    is_pending = Column(Binary)
    is_confirmed = Column(Binary)
    user_email = Column(String, ForeignKey('users.email'))
    quantity = Column(Float)
    item = Column(String)
    price = Column(float)
    willing_to_transport = Column(Binary)

    def __init__(self, requestId, user_email, quantity, item, price, willing_to_transport):
        self.offerId = Offer.offerId
        self.requestId = requestId
        self.user_email = user_email
        self.quantity = quantity
        self.item = item
        self.is_confirmed = False
        self.is_pending = True
        self.price = price
        self.willing_to_transport = willing_to_transport

    def __str__(self):
        return f'Offer {self.offerId} for request {self.requestId}'

    def json(self):
        return {'offerId': self.offerId,
                'requestId': self.requestId,
                'user_email': self.user_email,
                'quantity': self.quantity,
                'item': self.item,
                'is_confirmed': self.is_confirmed,
                'is_pending': self.is_pending,
                'price': self.price,
                'willing_to_transport': self.willing_to_transport}