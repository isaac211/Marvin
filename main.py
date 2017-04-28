from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit

import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    #specify local web page
    return render_template('index.html')

@socketio.on('connect')
def connect():
    print("Socket Connected");
    sys.stdout.flush()
    #send('event', 'Connected')

@socketio.on('event')
def event(msg):
    print(msg);
    sys.stdout.flush()

@socketio.on('disconnect')
def disconnect():
    print("Client disconnected")

if __name__=='__main__':
    socketio.run(app, host='0.0.0.0')
