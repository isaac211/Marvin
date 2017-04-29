from flask import Flask, render_template, Response
from flask_socketio import SocketIO, send, emit

import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WISM-SOCKET_lyoko_xana_3835%'
socketio = SocketIO(app)

COState = False

@app.route('/')
def index():
    #specify local web page
    return render_template('index.html')

@socketio.on('connect', namespace="/commsocket")
def connect():
    print("Socket Connected");
    sys.stdout.flush()

@socketio.on('disconnect', namespace="/commsocket")
def disconnect():
    print("Client disconnected")
    sys.stdout.flush()

@socketio.on_error(namespace="/commsocket")
def error(e):
    print("Error detected: " + str(e));
    sys.stdout.flush()

@socketio.on('event', namespace="/commsocket")
def event(msg):
    if (msg["type"] and msg["type"] == "move"):

        #TODO Matt, add your code for movement here!
        # msg["direction"] will have one of four values: "forward",
        # "backward", "left", or "right". This is flexible
        if (msg["direction"] == "forward"):
            pass
        if (msg["direction"] == "backward"):
            pass
        if (msg["direction"] == "left"):
            pass
        if (msg["direction"] == "right"):
            pass
        # Delete these lines after you're done:
        print("Moving " + msg["direction"])
        sys.stdout.flush()

    if (msg["type"] and msg["type"] == "co_req"):

        #TODO William, the CO percentage from the sensor here. This function
        # executes once per second, but we can make it faster if needed
        # Choose a threshold to trigger on. The indicator on the website
        # will turn red when the percentage is ABOVE this amount.
        COPercent = 0.5
        COThreshold = 0.8

        global COState
        next_state = False
        if (COPercent < COThreshold):
            next_state = False
        else:
            next_state = True

        if (next_state != COState):
            COState = next_state
            emit('event', {"type": "CO", "toggle": True}, namespace="/commsocket")

        # Delete this line after you're done:
        emit('event', {"type": "CO", "toggle": True}, namespace="/commsocket")

if __name__=='__main__':
    socketio.run(app, host='0.0.0.0')
