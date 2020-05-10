from flask_restplus import Namespace, Resource

from src import engine, session
from models.user import User
from models.request import Request
import urllib3
import json


api = Namespace('review', description='Review related operations')

parser1 = api.parser()
parser1.add_argument('email', location='args', default='email')

@api.route('/getuser')
class GetUserReview(Resource):
    """
    Retrieve all reviews for a single user.
    """

    @api.expect(parser1)
    def get(self):
        args = parser1.parse_args()
        email = args.get('email')

        #Need to test this query

        query = f'''select reviews.revOfferId, reviews.score, reviews.description from reviews
                    join
                    (Select offers.offerId, offers.user_email as "supplierEmailOff", offers.requestId from offers
                    join requests on (offers.requestId = requests.requestId)
                    where requests.is_surplus = 0) as SOff
                    on (reviews.revOfferId = SOff.offerId)
                    join
                    (Select offers.offerId, requests.user_email "supplierEmailReq", offers.requestId from offers
                    join requests on (offers.requestId = requests.requestId)
                    where requests.is_surplus = 1) as SReq
                    on (reviews.RevOfferId = SReq.offerId)
                    where ("{email}" = SReq.supplierEmailReq) or ("{email}" = SOff.supplierEmailOff)'''

        with engine.connect() as con:
            reviews = con.execute(query)
        
        for result in reviews:
            print(result)
        
        return {'response': 'success'}


@api.route('/getoffer')
class GetOfferReview(Resource):
    """
    Retrieve review for a given offer
    """
    parser = api.parser()
    parser.add_argument('offerId', location='args')

    @api.expect(parser)
    def get(self):
        args = RequestsGetUser.parser.parse_args()
        offerId = args.get('offerId')
        review4offer = session.query(Review).filter(Review.revOfferId == offerId).all()

        return {'response': review4offer}


@api.route('/create')
class CreateReview(Resource):
    """
    Create a new review for a given offer.
    """
    parser = api.parser()
    parser.add_argument('revOfferId', location='args', )
    parser.add_argument('score', location='args', default=0)
    parser.add_argument('description', location='args', default='')

    @api.expect(parser)
    def post(self):
        args = CreateReview.parser.parse_args()

        review = Review(revOfferId=args.get('revOfferId'), score=args.get('score'),
                          description=args.get('description'))
        session.add(review)
        session.commit()

        return {'response': 'success'}
