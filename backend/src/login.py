from flask_restplus import Namespace, Resource, fields
from src import bcrypt, engine, session
from ..models import User

api = Namespace('login', description='Login related operations')
parser = api.parser()

parser.add_argument('username', location='args', default='username')
parser.add_argument('password', location='args', default='password')
parser.add_argument('email', location='args', default='email')


@api.route('')
class LoginUser(Resource):

    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
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
