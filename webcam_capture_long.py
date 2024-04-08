# sudo -H pip3 install opencv-python
# sudo -H pip3 install numpy

# This script opens a stream and saves frames every 30s some other long duration. The stream is opened and closed for each frame capture to prevent overread but does mean a new request occurs for every single frame. See other script for shorter duration captures.

import cv2
import time
import numpy as np

url = 'http://site.com/video.mjpg'

while True:
  capture = cv2.VideoCapture(url)
  seconds = time.time()  # time since unix epoch in seconds
  ret, frame = capture.read()
  height, width, channels = frame.shape
  if (ret == True) and (height > 0) and (width > 0): # if a valid frame captured
    cv2.imwrite("Cam_Stream_Frame_" + str(seconds) + ".jpg", frame)
    print("created image: " + "Cam_Stream_Frame_" + str(seconds) + ".jpg")
    capture.release()  # prevents overread, last frame in buffer being stuck, also minimizes bandwidth usage
    time.sleep(30)  # save frame every X seconds
  elif frame == None: # if frame empty
    print("Empty Frame")    
    capture.release()  # prevents overread, last frame in buffer being stuck, also minimizes bandwidth usage
    time.sleep(10)  # try again in 10 seconds
  else:
    print("Read Failed") # if return value of False during capture.read
    capture.release()  # prevents overread, last frame in buffer being stuck, also minimizes bandwidth usage
    time.sleep(10)  # try again in 10 seconds
