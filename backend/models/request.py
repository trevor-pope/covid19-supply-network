from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Binary, Float

Base = declarative_base()


class Request(Base):
    __tablename__ = 'requests'

    requestId = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String, ForeignKey('users.email'))
    min_quantity = Column(Float)
    quantity = Column(Float)
    urgency = Column(Integer)
    item = Column(String)
    fulfilled = Column(Binary)
    is_surplus = Column(Binary)

    def __init__(self, user_email, quantity, item, urgency, is_surplus):
        self.requestId = Request.requestId
        self.user_email = user_email
        self.quantity = quantity
        self.item = item
        self.urgency = urgency
        self.fulfilled = False
        self.is_surplus = is_surplus

    # Note, we pull Request.requestID because we let it autoincrement,
    # but it only updates after the new request has been committed to the db, so we wary of that I guess. -Trevor
    def __str__(self):
        return f'Request {self.requestId} from {self.user_email} (MAY NOT BE UNIQUE UNTIL DB COMMIT)'

    def json(self):
        return {'requestID': self.requestId,
                'user_email': self.user_email,
                'quantity': self.quantity,
                'item': self.item,
                'urgency': self.urgency,
                'fulfilled': self.fulfilled,
                'is_surplus': self.is_surplus}


