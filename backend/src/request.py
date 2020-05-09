from flask_restplus import Namespace, Resource
from src import session
from models import User, Request
import urllib3
import json

api = Namespace('request', description='Request related operations')


@api.route('/getuser')
class RequestsGetUser(Resource):
    request_parser = api.parser()
    request_parser.add_argument('email', location='args')

    @api.expect(request_parser)
    def get(self):
        args = RequestsGetUser.request_parser.parse_args()
        email = args.get('email')
        requests_from_user = session.query(Request).filter(Request.user_email == email).all()

        return {'response': requests_from_user}


@api.route('/getall')
class RequestsGetAll(Resource):
    request_parser = api.parser()
    request_parser.add_argument('email', location='args')
    request_parser.add_argument('sort', location='args')
    request_parser.add_argument('item_filter', location='args')

    @api.expect(request_parser)
    def get(self):
        ZIPCODE_API_KEY = 'iMVNI7irDtVXi3aqsMoMpFfIYswPzoqVlDWyljkxbZg7YYicJ1ihpVBcr6dnMfrU'
        args = RequestsGetAll.request_parser.parse_args()
        email, sort, item_filter = args.get('email'), args.get('sort'), args.get('item_filter')

        requests = session.query(Request)
        if item_filter is not None:
            requests = requests.filter(Request.item == item_filter)  # == for now, should probably be an approximate match

        requests = requests.all()

        if sort in ['distance', None]:
            user_zip = session.query(User).filter(User.email == email)[0].zipcode
            http = urllib3.PoolManager()

            def get_distance(request):
                request_zip = session.query(User).filter(User.email == request.user_email)[0].zipcode
                url = f"https://www.zipcodeapi.com/rest/{ZIPCODE_API_KEY}/distance.json/{user_zip}/{request_zip}/miles"
                r = http.request('GET', url)
                distance = json.loads(r.data.decode('utf-8'))['distance']

                return distance

            requests = sorted(requests, key=get_distance)

        return {'response': requests}

register_parser = api.parser()

register_parser.add_argument('fname', location='args', default='fname')
register_parser.add_argument('lname', location='args', default='lname')
register_parser.add_argument('username', location='args', default='username')
register_parser.add_argument('password', location='args', default='password')
register_parser.add_argument('email', location='args', default='email')

@api.route('/add')
class RequestAdd(Resource):

    @api.expect(register_parser)
    def post(self):
        args = register_parser.parse_args()
        print(args)

        return {'response': 'success'}
