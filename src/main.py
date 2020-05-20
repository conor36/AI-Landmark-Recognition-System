import uuid
from datetime import datetime
from flask import (
    Flask,
    request,
    jsonify
    )

from PIL import Image  
import PIL 

from generateContent import BuildingData

app = Flask(__name__) # app = flask.Flask(__name__)
file = '..\assets'
app.config['file'] = file

users = []
chat = [] # Holds message ids
images = dict()
predictionID = ''
id = None

data = BuildingData()

@app.route("/")
def hello():
    return "hello\n"

@app.route("/login",methods=["POST"])
def login():
    print("Hello")
    username = request.json.get('username',None)
    user_taken = username in users
    if username is None or user_taken:
        abort(401)
    else:
        users.append(username)
        return jsonify({
            'status':'ok',
            'message':'logged in',
            })
    


# send image
@app.route("/send",methods=["POST"])
def send():
        predictionID = request.json.get('predictionID',None)
        id = predictionID[1:-1]
        #print(id)
        return id


@app.route("/getContent/<id>",methods=["GET"])
def get(id):
    
    print(id)
    result = data.getData(id)
    print(result)

    return result



   


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')