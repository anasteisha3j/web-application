from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Column, ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
    
class Image(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    picture = db.Column(db.LargeBinary, nullable=False)  
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    images = db.relationship('Image')
    def get_id(self):
        return str(self.id)