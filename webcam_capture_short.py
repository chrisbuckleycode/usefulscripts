# sudo -H pip3 install opencv-python

# This script opens a stream and saves frames every 1s, 5s or some other short duration. Use only for short captures of 1 to 2 minutes as overread will occur. See other script for time lapse over longer duration

import cv2
import time

url = 'http://site.com/video.mjpg'

capture = cv2.VideoCapture(url)

while True:
  seconds = time.time()  # time since unix epoch in seconds
  ret, frame = capture.read()
  cv2.imwrite("Cam_Stream_Frame_" + str(seconds) + ".jpg", frame)
  time.sleep(60)  # save frame every 60 seconds
