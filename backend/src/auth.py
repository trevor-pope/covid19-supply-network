from flask_restplus import Namespace, Resource
from src import bcrypt, session
from models.user import User

api = Namespace('auth', description='Authentication related operations')

login_parser = api.parser()
login_parser.add_argument('username', location='args', default='username')
login_parser.add_argument('password', location='args', default='password')
login_parser.add_argument('email', location='args', default='email')

@api.route('/login')
class LoginUser(Resource):

    @api.expect(login_parser)
    def get(self):
        args = login_parser.parse_args()
        print(args)

        username = args.get('username')
        password = args.get('password')
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
register_parser.add_argument('zipcode', location='args', default='90210')

@api.route('/register')
class RegisterUser(Resource):

    @api.expect(register_parser)
    def post(self):
        args = register_parser.parse_args()
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
            zipcode = args.get('zipcode')

            user = User(username=username, password=pwd_hash, email=args.get('email'), zipcode=zipcode)
            print(user)
            session.add(user)
            session.commit()

            return {'response': 'success'}


profile_parser = api.parser()
profile_parser.add_argument('email', location='args', default='email')


@api.route('/profile')
class ViewUser(Resource):

    @api.expect(profile_parser)
    def get(self):
        args = profile_parser.parse_args()
        print(args)
        email = args.get('email')

        user_res = session.query(User).filter(User.email.like(f'%{email}%')).all()[0]

        return user_res.json()
