import RPi.GPIO as io
io.setmode(io.BOARD)
import sys, tty, termios, time

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

motor1_in1_pin = 7
motor1_in2_pin = 11

motor2_in1_pin = 32
motor2_in2_pin = 36 


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
    io.output(motor1_in1_pin, io.HIGH)
    io.output(motor1_in2_pin, io.LOW)

def motor1_reverse():
    io.output(motor1_in1_pin, io.LOW)
    io.output(motor1_in2_pin, io.HIGH)

def motor2_forward():
    io.output(motor2_in1_pin, io.HIGH)
    io.output(motor2_in2_pin, io.LOW)

def motor2_reverse():
    io.output(motor2_in1_pin, io.LOW)
    io.output(motor2_in2_pin, io.HIGH)

#PWM pins set to false by default
io.output(motor1_in1_pin, io.LOW)
io.output(motor1_in2_pin, io.LOW)
io.output(motor2_in1_pin, io.LOW)
io.output(motor2_in2_pin, io.LOW)

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
        motor1_forward()
    if(char == "s"):
        motor1_reverse()
    if(char == "a"):
        motor2_forward()
    if(char == "d"):
        motor2_reverse()
    if(char == "x"):
        print("Program Ended")
        break

    char = ""


io.cleanup()
