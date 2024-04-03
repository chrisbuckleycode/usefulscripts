#!/usr/bin/env python

# sudo -H pip3 install opencv-python
# sudo -H pip3 install numpy

# This script opens a stream and saves frames every 30s some other long duration. The stream is opened and closed for each frame capture to prevent overread but does mean a new request occurs for every single frame. See other script for shorter duration captures.

import cv2
import time
import numpy as np

def my_function(*site_urls):
    number_of_urls = len(site_urls)

    site_urls = list(site_urls)
    for i in range(1, number_of_urls + 1):    
        print(site_urls[i - 1])

    while True:
        
        for site_number in range(1, number_of_urls + 1):
            
            url = site_urls[site_number - 1]     
            capture = cv2.VideoCapture(url)
            seconds = time.time()  # time since unix epoch in seconds
            ret, frame = capture.read()
            height, width, channels = frame.shape

            if (ret == True) and (height > 0) and (width > 0): # if a valid frame captured
                cv2.imwrite("Site_" + str(site_number) + "_Cam_Stream_Frame_" + str(seconds) + ".jpg", frame)
                print("created image: " + "Site_" + str(site_number) + "_Cam_Stream_Frame_" + str(seconds) + ".jpg")
                capture.release()  # prevents overread, last frame in buffer being stuck, also minimizes bandwidth usage
            elif frame == None: # if frame empty
                print("Empty Frame")    
                capture.release()  # prevents overread, last frame in buffer being stuck, also minimizes bandwidth usage
            else:
                print("Read Failed") # if return value of False during capture.read
                capture.release()  # prevents overread, last frame in buffer being stuck, also minimizes bandwidth usage
               
        time.sleep(30)  # save frame every X seconds  

    
sites = ("http://site1/mjpg/video.mjpg", "http://site2/mjpg/video.mjpg", "http://site3/mjpg/video.mjpg")
# add here as many urls as you want

my_function(*sites)

