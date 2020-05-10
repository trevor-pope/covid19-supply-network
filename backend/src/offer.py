from flask_restplus import Namespace, Resource
from src import session
from models.user import User
from models.request import Request
from models.offer import Offer
import urllib3
import json

api = Namespace('offer', description='Offer related operations')


@api.route('/create')
class CreateOffer(Resource):
    """
    Create a new offer for a request from a given user.
    """
    parser = api.parser()
    for arg in ['requestId', 'user_email', 'quantity', 'price', 'willing_to_transport', 'image']:
        parser.add_argument(arg, location='args')

    @api.expect(parser)
    def post(self):
        args = CreateOffer.parser.parse_args()
        offer = Offer(user_email=args.get('user_email'), quantity=args.get('quantity'),
                      requestId=args.get('requestId'), price=args.get('price'),
                      willing_to_transport=args.get('willing_to_transport'), image=args.get('image'))
        session.add(offer)
        session.commit()

        return {'response': 'success'}


@api.route('/getAllOffersByRequest')
class GetAllOffersByRequest(Resource):
    """
    Retrieve all offers for a specific request
    """
    parser = api.parser()
    parser.add_argument('requestId', location='args', required=True)
    parser.add_argument('pending_only', location='args')

    @api.expect(parser)
    def get(self):
        args = GetAllOffersByRequest.parser.parse_args()
        requestId, pending_only = args.get('requestId'), args.get('pending_only')

        offers = session.query(Offer).filter(Offer.requestId == requestId)
        if pending_only:
            offers = offers.filter(Offer.is_pending == True)

        return {'response': [offer.json() for offer in offers]}


@api.route('/getUserOffers')
class GetAllOffersByUser(Resource):
    """
    Retrieve all offers that a User has made.
    """
    parser = api.parser()
    parser.add_argument('email', location='args', required=True)
    parser.add_argument('pending_only', location='args')

    @api.expect(parser)
    def get(self):
        args = GetAllOffersByRequest.parser.parse_args()
        requestId, pending_only = args.get('requestId'), args.get('pending_only')

        offers = session.query(Offer).filter(Offer.requestId == requestId)
        if pending_only:
            offers = offers.filter(Offer.is_pending == True)

        return {'response': [offer.json() for offer in offers]}


@api.route('/confirm')
class SetConfirmed(Resource):
    """
    Confirm an offer from a given User.
    """
    parser = api.parser()
    parser.add_argument('offerId', location='args', required=True)
    parser.add_argument('confirm', location='args', required=True)

    @api.expect(parser)
    def post(self):
        args = SetConfirmed.parser.parse_args()
        session.query(Offer).filter(Offer.offerId == args.get('offerId')).update({'isConfirmed': args.get('confirm')})
        session.query(Offer).filter(Offer.offerId == args.get('offerId')).update({'isPending': False})

        offer = session.query(Offer).filter(Offer.offerId == args.get('offerId')).first()
        offer_request = session.query(Request).filter(Request.requestId == offer.requestId).first()
        if offer_request.quantity < offer.quantity:
            session.query(Request).filter(Request.requestId == offer.requestId).\
                update({'quantity': offer_request.quantity - offer.quantity})
        else:
            session.query(Request).filter(Request.requestId == offer.requestId). \
                update({'fulfilled': True})

        session.commit()

        return {'response': 'success'}