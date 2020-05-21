# sudo -H pip3 install opencv-python

# This script opens a stream and saves frames every 30s some other long duration. The stream is opened and closed for each frame capture to prevent overread but does mean a new request occurs for every single frame. See other script for shorter duration captures.

import cv2
import time

url = 'http://site.com/video.mjpg'

while True:
  capture = cv2.VideoCapture(url)
  seconds = time.time()  # time since unix epoch in seconds
  ret, frame = capture.read()
  cv2.imwrite("Cam_Stream_Frame_" + str(seconds) + ".jpg", frame)
  capture.release()  # prevents overread, last frame in buffer being stuck, also minimizes bandwidth usage
  time.sleep(60)  # save frame every 60 seconds
