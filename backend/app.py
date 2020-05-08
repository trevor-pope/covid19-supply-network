from flask import Flask, redirect, url_for
from flask_restplus import Api
from src import app

api = Api(app)

from src.streams import api as api_streams
from src.login import api as api_login
from src.register import api as api_register

api.add_namespace(api_streams)
api.add_namespace(api_login)
api.add_namespace(api_register)

if __name__ == '__main__':
    app.run(debug=True)
