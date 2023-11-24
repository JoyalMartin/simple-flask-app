from flask import Flask,jsonify,request 
from flask_cors import CORS
from flask_socketio import SocketIO,emit



app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")



@socketio.on('connect')
def test_connect():
    print("connected")
    emit('my_response', {"data": "connected"})
  
if __name__=='__main__': 
    socketio.run(app, debug=True)