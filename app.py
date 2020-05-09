from flask import Flask, redirect, url_for
from flask_restplus import Api
from src import app

api = Api(app)


from src.auth import api as api_auth
from src.request import api as api_request
from src.viewprofile import api as api_viewprofile

api.add_namespace(api_auth)
api.add_namespace(api_request)
api.add_namespace(api_viewprofile)

if __name__ == '__main__':
    app.run(debug=True)
