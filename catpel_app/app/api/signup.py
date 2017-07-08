from . import api
from .. import db
from flask import request
from flask import jsonify
from ..models import User

@api.route('/signup/',methods=['POST'])
def signup():
    if request.method == 'POST':
        pass
