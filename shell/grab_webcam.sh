#!/usr/bin/env bash
# https://zxq9.com/archives/795
# this downloads a new image from a web cam every second
# sudo apt-get install imagemagick
# convert -resize 640x480 -delay 20 -loop 0 cam_image*.jpg myimage.gif

image_url="http://blabla.com/webcamimage.jpg"
while [ true ]
do
  wget $image_url --output-document=./cam_image_`date +%s`.jpg
  sleep 10
done
