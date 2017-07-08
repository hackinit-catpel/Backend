# coding:utf-8

"""
sql models

use: Flask-SQLAlchemy
-- http://flask-sqlalchemy.pocoo.org/2.1/

"""


from flask import current_app,request
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_passwor
d_hash
from flask_login import UserMixin, AnonymousUserMixin, current_user
from wtforms.validators import Email
from itsdangerous import JSONWebSignatureSerializer as Serializer

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Interger,primary_key=True)
    username = db.Column(db.String(164), unique=True, index=True)
    password_hash = db.Column(db.String(164))
    time = db.Column(db.Float)
    forgive_time = db.Column(db.Integer,default=5)
    

class AnonymousUser(AnonymousUserMixin):
    """ anonymous user """
    def is_admin(self):
        return False

login_manager.anonymous_user = AnonymousUser
