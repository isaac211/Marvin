from flask import Flask, render_template, Response
from flask_socketio import SocketIO, send, emit

import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WISM-SOCKET_lyoko_xana_3835%'
socketio = SocketIO(app)

@app.route('/')
def index():
    #specify local web page
    return render_template('index.html')

@socketio.on('connect', namespace="/commsocket")
def connect():
    print("Socket Connected");
    sys.stdout.flush()

@socketio.on('event', namespace="/commsocket")
def event(msg):
    print(msg);
    sys.stdout.flush()
    emit('event', 'Received')

@socketio.on('disconnect', namespace="/commsocket")
def disconnect():
    print("Client disconnected")
    sys.stdout.flush()

if __name__=='__main__':
    socketio.run(app, host='0.0.0.0')
