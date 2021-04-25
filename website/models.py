from . import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = "users"

    # this is the schema
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    squat_max = db.Column(db.Integer, default=0)
    clean_max = db.Column(db.Integer, default=0)
    snatch_max = db.Column(db.Integer, default=0)
    




