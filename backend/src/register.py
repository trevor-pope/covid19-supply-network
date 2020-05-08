from flask_restplus import Namespace, Resource, fields
from src import bcrypt, session
from models import User

api = Namespace('register', description='Registration related operations')
parser = api.parser()

parser.add_argument('fname', location='args', default='fname')
parser.add_argument('lname', location='args', default='lname')
parser.add_argument('username', location='args', default='username')
parser.add_argument('password', location='args', default='password')
parser.add_argument('email', location='args', default='email')


@api.route('')
class RegisterUser(Resource):

    @api.expect(parser)
    def post(self):
        args = parser.parse_args()
        print(args)

        username = args.get('username')
        # find if username exists
        results = session.query(User).filter(User.username == username)

        if results.count() > 0:
            print('user already found')

            return {'response': 'failure', 'reason': 'User already exists'}
        else:
            print('user not found, creating new account')

            password = args.get('password')
            pwd_hash = bcrypt.generate_password_hash(password)

            user = User(username=username, password=pwd_hash, email=args.get('email'))
            print(user)
            session.add(user)
            session.commit()

            return {'response': 'success'}
