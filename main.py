from flask import Flask, render_template, Response
from flask_socketio import SocketIO, send, emit
from vidstream import camera
import RPi.GPIO as io
io.setmode(io.BOARD)
import sys, tty, termios, time

io.setup(7, io.OUT)
io.setup(11, io.OUT)
io.setup(32, io.OUT)
io.setup(36, io.OUT)

motor1_in1_pin = 7
motor1_in2_pin = 11

motor2_in1_pin = 32
motor2_in2_pin = 36

#PWM pins set to false by default
io.output(motor1_in1_pin, io.LOW)
io.output(motor1_in2_pin, io.LOW)
io.output(motor2_in1_pin, io.LOW)
io.output(motor2_in2_pin, io.LOW)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WISM-SOCKET_lyoko_xana_3835%'
socketio = SocketIO(app)

COState = False

#Motor direction controls.
def motor1_forward():
    io.output(motor1_in1_pin, io.HIGH)
    io.output(motor1_in2_pin, io.LOW)

def motor1_reverse():
    io.output(motor1_in1_pin, io.LOW)
    io.output(motor1_in2_pin, io.HIGH)

def motor2_forward():
    io.output(motor2_in1_pin, io.HIGH)
    io.output(motor2_in2_pin, io.LOW)
    io.output(motor1_in1_pin, io.HIGH)

def motor2_reverse():
    io.output(motor2_in1_pin, io.LOW)
    io.output(motor2_in2_pin, io.HIGH)
    io.output(motor1_in1_pin, io.HIGH)

def stop_motors():
    io.output(motor1_in1_pin, io.LOW)
    io.output(motor1_in2_pin, io.LOW)
    io.output(motor2_in1_pin, io.LOW)
    io.output(motor2_in2_pin, io.LOW)

@app.route('/')
def index():
    #specify local web page
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')    
@app.route('/video_feed')
def video_feed():
    return Response(gen(camera()),
            mimetype='multipart/x-mixed-replace; boundary=frame')

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
        if (msg["direction"] == "forward"):
            stop_motors()
            motor1_forward()
        if (msg["direction"] == "backward"):
            stop_motors()
            motor1_reverse()
        if (msg["direction"] == "left"):
            motor2_forward()
        if (msg["direction"] == "right"):
            motor2_reverse()
        if (msg["direction"] == "stop"):
            stop_motors()
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
