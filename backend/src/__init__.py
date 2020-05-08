from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import *

app = Flask(__name__)
app.config.from_object(Config())
CORS(app)

db = SQLAlchemy(app)
