from flask_restplus import Namespace, Resource
from src import bcrypt, session
from models import User

api = Namespace('profile', description='View User Profiles')


@api.route('/viewprofile')  # was thinking of using f'/{UserName}' here is that doable?
class ViewUser(Resource):
    user_parser = api.parser()
    user_parser.add_argument('username', location='args')

    @api.expect(user_parser)
    def get(self):
        args = ViewUser.user_parser.parse_args()
        username = args.get('username')

        search = '%{}%'.format(username)
        UserRes = session.query(User).filter(User.like(search)).all()[0]

        return UserRes.json()



