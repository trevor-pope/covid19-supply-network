from flask import Flask, redirect, url_for
from flask_restplus import Api
from src import app

api = Api(app)

from src.streams import api as api_main

api.add_namespace(api_main)

if __name__ == '__main__':
    app.run(debug=True)
