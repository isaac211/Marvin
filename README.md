# Marvin

Dependencies

pip install numpy
pip install "picamera[array]"
pip install Flask
pip install Flask-SocketIO
pip install opencv-python

PiCamera needs to be recognized as default device using
sudo modprobe bcm2835-v4l2


Also need to connect a camera somehow.
When running the server on windows laptop, it seems to automatically grab
the laptop camera.

Run start.sh to host the page on your current IP port 5000.

Tested on Firefox for Windows and iPhone.
