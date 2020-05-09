from flask_restplus import Namespace, Resource
from src import bcrypt, session
from models.user import User

api = Namespace('review', description='Review related operations')
parser1 = api.parser()

parser1.add_argument('email', location='args', default='email')

@api.route('/view')
class ViewReviews(Resource):

    @api.expect(parser1)
    def get(self):
        args = parser1.parse_args()
        print(args)

        username = args.get('email')
        pwd_hash = bcrypt.generate_password_hash(password)

        users = session.query(User).filter(
            User.username == username).all()

        if len(users) > 0:
            user = users[0]
            correct = bcrypt.check_password_hash(user.password, password)

            if correct: 
                return {'response': 'success'}
            else:
                return {'response': 'bad password'}

        return {'response': 'no user found'}

register_parser = api.parser()

register_parser.add_argument('fname', location='args', default='fname')
register_parser.add_argument('lname', location='args', default='lname')
register_parser.add_argument('username', location='args', default='username')
register_parser.add_argument('password', location='args', default='password')
register_parser.add_argument('email', location='args', default='email')

@api.route('/add')
class RegisterUser(Resource):

    @api.expect(register_parser)
    def post(self):
        args = register_parser.parse_args()
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
