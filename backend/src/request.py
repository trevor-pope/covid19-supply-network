from flask_restplus import Namespace, Resource
from src import session
from models.user import User
from models.request import Request
import urllib3
import json

api = Namespace('request', description='Request related operations')


@api.route('/getuser')
class RequestsGetUser(Resource):
    """
    Retrieve all requests for a single user.
    """
    parser = api.parser()
    parser.add_argument('email', location='args')

    @api.expect(parser)
    def get(self):
        args = RequestsGetUser.parser.parse_args()
        email = args.get('email')
        requests_from_user = session.query(Request).filter(Request.user_email == email).all()

        return {'response': requests_from_user}


@api.route('/getall')
class RequestsGetAll(Resource):
    """
    Retrieve all requests from all users, with optional sorting and searching parameters.
    """
    parser = api.parser()
    for arg in ['email', 'sort', 'item_filter']:
        parser.add_argument(arg, location='args')

    @api.expect(parser)
    def get(self):
        ZIPCODE_API_KEY = "iMVNI7irDtVXi3aqsMoMpFfIYswPzoqVlDWyljkxbZg7YYicJ1ihpVBcr6dnMfrU"
        args = RequestsGetAll.parser.parse_args()
        email, sort, item_filter = args.get('email'), args.get('sort'), args.get('item_filter')

        requests = session.query(Request)
        if item_filter is not None:
            requests = requests.filter(
                Request.item == item_filter)  # == for now, should probably be an approximate match

        requests = requests.all()

        if sort in ['distance', None]:  # By default, sort by distance
            user_zip = session.query(User).filter(User.email == email)[0].zipcode
            http = urllib3.PoolManager()

            def get_distance(request):
                request_zip = session.query(User).filter(User.email == request.user_email)[0].zipcode
                url = f"https://www.zipcodeapi.com/rest/{ZIPCODE_API_KEY}/distance.json/{user_zip}/{request_zip}/miles"
                r = http.request('GET', url)
                distance = json.loads(r.data.decode('utf-8'))['distance']

                return distance

            requests = sorted(requests, key=get_distance)
            print(requests)
            print([request.json() for request in requests])

        return {'response': [request.json() for request in requests]}


@api.route('/create')
class CreateRequest(Resource):
    """
    Create a new request for a given user.
    """
    parser = api.parser()
    parser.add_argument('user_email', location='args', default='email')
    parser.add_argument('min_quantity', location='args', default=0)
    parser.add_argument('quantity', location='args', default=0)
    parser.add_argument('urgency', location='args', default=0)
    parser.add_argument('item', location='args', default='mask')

    @api.expect(parser)
    def post(self):
        args = CreateRequest.parser.parse_args()

        request = Request(user_email=args.get('user_email'), min_quantity=args.get('min_quantity'),
                          quantity=args.get('quantity'), urgency=args.get('urgency'), item=args.get('item'))
        session.add(request)
        session.commit()

        return {'response': 'success'}
