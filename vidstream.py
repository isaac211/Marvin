#vidstream.py
import cv2

class camera(object):
    def __init__(self):
        #OpenCV will capture from device 0
        #Can use video file isntead
        self.video = cv2.VideoCapture(0)
        if self.video.isOpened() == False:
            print ("Camera not open!")

    def __del__(self):
        #shut off feed
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        if not success:
            print("Failed to capture!")
        #Set motion JPG as capture standard
        ret, jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()
