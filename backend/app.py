from flask import Flask, redirect, url_for
from flask_restplus import Api
from src import app

api = Api(app)

from src.streams import api as api_streams
from src.auth import api as api_auth

api.add_namespace(api_streams)
api.add_namespace(api_auth)

if __name__ == '__main__':
    app.run(debug=True)
