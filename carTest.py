import RPi.GPIO as io
io.setmode(io.BCM)
import sys, tty, termios, time

#PWM settings
motor1_in1_pin = 27 
motor1_in2_pin = 17
io.setup(motor1_in1_pin, io.OUT)
io.setup(motor1_in2_pin, io.OUT)
motor1 = io.PWM(4,100)
motor1.start(0)
motor1.ChangeDutyCycle(0)

motor2_in1_pin = 12
motor2_in2_pin = 16 
io.setup(motor2_in1_pin, io.OUT)
io.setup(motor2_in2_pin, io.OUT)
motor2 = io.PWM(4,100)
motor2.start(0)
motor2.ChangeDutyCycle(0)


#get user input 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    print (ch)
    return ch

#Motor direction controls.
def motor1_forward():
    io.output(motor1_in1_pin, True)
    io.output(motor1_in2_pin, False)

def motor1_reverse():
    io.output(motor1_in1_pin, False)
    io.output(motor1_in2_pin, True)

def motor2_forward():
    io.output(motor2_in1_pin, True)
    io.output(motor2_in2_pin, False)

def motor2_reverse():
    io.output(motor2_in1_pin, False)
    io.output(motor2_in2_pin, True)


def toggleSteering(direction):

    global wheelStatus

    if(direction == "right"):
        if(wheelStatus == "center"):
            motor1_forward()
            motor1.ChangeDutyCycle(99)
            wheelStatus = "right"
        elif(wheelStatus == "left"):
            motor1.ChangeDutyCycle(0)
            wheelStatus = "center"

    if(direction == "left"):
        if(wheelStatus == "center"):
            motor1_reverse()
            motor1.ChangeDutyCycle(99)
            wheelStatus = "left"
        elif(wheelStatus == "right"):
            motor1.ChangeDutyCycle(0)
            wheelStatus = "center"

#PWM pins set to false by default
io.output(motor1_in1_pin, False)
io.output(motor1_in2_pin, False)
io.output(motor2_in1_pin, False)
io.output(motor2_in2_pin, False)

wheelStatus = "center"

print("w/s: acceleration")
print("a/d: steering")
print("x: exit")
#control loop
while True:
    #wasd controls 
    #x to exit
    #char is user input
    char = getch()

    if(char == "w"):
        motor2_forward()
        motor2.ChangeDutyCycle(99)

    if(char == "s"):
        motor2_reverse()
        motor2.ChangeDutyCycle(99)

    if(char == "a"):
        toggleSteering("left")

    if(char == "d"):
        toggleSteering("right")

    if(char == "x"):
        print("Program Ended")
        break

    motor2.ChangeDutyCycle(0)

    char = ""


io.cleanup()
