from mq import *
import sys, time

# This is the code that would have run for the CO sensor had the ADC not been burnt out. Right now, in the code, we do have code that pushes values to the webpage, which would have been the way the CO values would have been sent, so the networking portion had been completed, and it was only due to hardware issues that the actual CO sensor wasn't read.

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("CO: %g ppm" % (perc["CO"]))
        sys.stdout.flush()
        time.sleep(0.1)

except:
    print("\nAbort by user")