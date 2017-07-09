from flask import jsonify ,request
from ..  import db
from ..models import User
from . import api
import json
import os

@api.route('/sendinfo/',methods=['POST'])
def send_info():
    if request.method == 'POST':
        my_id = int(request.get_json().get('my_id'))
        user = User.query.filter_by(id=my_id).first()
        the_id = user.bind_id
        info = str(request.get_json().get('info'))

        if os.path.isdir("Message"):
            pass
        else:
            os.mkdir("Message")

        if os.path.isdir("Message/"+str(the_id)):
            pass
        else:
            os.mkdir("Message/"+str(the_id))

        if os.path.isfile("Message/"+str(the_id)+"message"):
            pass
        else:
            os.mknod("Message/"+str(the_id)+"message")

        mess_file = open("Message/"+str(the_id)+"message","w")
        mess_file.writelines(
            [
                "message:" + info +"\n",
                "bind_id:" + my_id + "\n",
                "havent"
            ]
        )

        return jsonify({
            "status":200
        })
