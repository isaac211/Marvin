from flask import Flask, render_template, Response
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS, cross_origin

import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app)

@app.route('/')
@cross_origin()
def index():
    #specify local web page
    return render_template('index.html')

@socketio.on('connect')
def connect():
    print("Socket Connected");
    sys.stdout.flush()

@socketio.on('event')
def event(msg):
    print(msg);
    sys.stdout.flush()
    emit('event', 'Received')

@socketio.on('disconnect')
def disconnect():
    print("Client disconnected")

if __name__=='__main__':
    socketio.run(app, host='0.0.0.0')
