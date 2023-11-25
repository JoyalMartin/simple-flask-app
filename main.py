from flask import Flask,jsonify,request 
from flask_cors import CORS
from flask_socketio import SocketIO,emit
import random
import time


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")



@socketio.on('connect')
def test_connect():
    print("connected")
    emit('my_response', {"data": "connected"})


@socketio.on('getdata')
def sendtempData():
    print("Event received")
    temps = [24,23.9,22.3,24.1, 22.5,24.2]
    i = 0
    while i <= 100:
        print("temp data")
        emit('temp', {"data": str(random.choice(temps))})
        time.sleep(2)
        i += 1

@socketio.on('getperc')
def sendPercData():
    print("Event received")
    temps = [80, 90, 100, 70, 95, 85, 77, 82, 83]
    i = 0
    while i <= 100:
        print("temp data")
        emit('perc', {"data": str(random.choice(temps))})
        time.sleep(2)
        i += 1
  
if __name__=='__main__': 
    socketio.run(app, debug=True)