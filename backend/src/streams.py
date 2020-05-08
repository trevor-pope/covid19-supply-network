from flask import send_from_directory, request
from flask_restplus import Namespace, Resource, fields
from src import db
from .clean import clean

api = Namespace('main', description='Main app operations')
parser = api.parser()

# parser.add_argument('username', location='args', default='username')
# parser.add_argument('password', location='args', default='password')
# parser.add_argument('email', location='args', default='email')


@api.route('')
class Streams(Resource):

    @api.expect(parser)
    def get(self):
        conn = db.get_engine()
        query = conn.execute("select * from table")
        rows = []
        for row in query:
            row = dict(row)
            if row['date'] is not None:
                row['date'] = row['date'].strftime('%m/%d/%Y')
            rows.append(row)

        return rows


@api.route('/download')
class Download(Resource):

    @api.expect(parser)
    def get(self):
        return send_from_directory('../data', 'data.csv')


@api.route('/upload')
class Upload(Resource):

    @api.expect(parser)
    def post(self):
        csv = request.files['file']
        csv.save(f'new_data/{csv.filename}')

        df = clean(f'new_data/{csv.filename}')
        df.to_sql('table', db.get_engine(), index=False, if_exists='append')
        return 'received'
