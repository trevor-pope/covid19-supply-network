from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Binary, Float

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'

    revOfferId = Column(Integer, ForeignKey('offers.offerId'), primary_key=True)
    score = Column(Integer)
    description = Column(String)

    def __init__(self, revOfferId, score, description):
        self.revOfferId = revOfferId
        self.score = score
        self.description = description

    def __str__(self):
        return f'{self.revOfferId} received a review score of {self.score} \n Description of Review: \n {self.description}'

    def json(self):
        return {'revOfferId': self.,revOfferId
                'score': self.score,
                'description': self.description}