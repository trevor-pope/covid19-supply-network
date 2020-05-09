from flask_restplus import Namespace, Resource
from src import bcrypt, session
from models import User

api = Namespace('request', description='Request related operations')
login_parser = api.parser()

login_parser.add_argument('username', location='args', default='username')
login_parser.add_argument('password', location='args', default='password')
login_parser.add_argument('email', location='args', default='email')

@api.route('/get')
class RequestGet(Resource):

    @api.expect(login_parser)
    def get(self):
        args = login_parser.parse_args()
        print(args)

        return {'response': 'no user found'}

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
