from flask import Flask, redirect, url_for
from flask_restplus import Api
from src import app

api = Api(app)

from src.streams import api

api.add_namespace(api)

if __name__ == '__main__':
    app.run(debug=True)
