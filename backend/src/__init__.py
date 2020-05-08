from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from config import *

app = Flask(__name__)
app.config.from_object(Config())
CORS(app)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
engine = db.create_engine(DATABASE_URL, {})
Session = sessionmaker(bind=engine)
session = Session()
