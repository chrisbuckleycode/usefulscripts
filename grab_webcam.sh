#!/bin/bash
# https://zxq9.com/archives/795
# this downloads a new image from a web cam every second
image_url="http://blabla.com/webcamimage.jpg"
while [ true ]
do
  wget $image_url --output-document=./cam_image_`date +%s`.jpg
  sleep 10
done
