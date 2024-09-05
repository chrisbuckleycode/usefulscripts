## FILE: crop_image_top.py
##
## DESCRIPTION: Crops image using Pillow for custom use case.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: python3 crop_image_top.py
##

# TODO(chrisbuckleycode): Move comments to README.md

# after cropping, convert to animated gif with imagemagick:
# convert -delay 6 -loop 0 *.jpg animated.gif
# optional to resize for sending via mobile:
# convert animated.gif -resize 533x287 animated2.gif


from PIL import Image
import os

pixels_to_chop_from_top = 20

path = 'images/'               # put images in directory called images
listing = os.listdir(path)
for infile in listing:
    path_plus_filename = os.path.join(path,infile) 
    file_root, file_ext = os.path.splitext(infile)
    im = Image.open(path_plus_filename)
    cropped = im.crop((0, pixels_to_chop_from_top, 800, 450)) # left, upper, right, lower; image size is 800 x 450 px
#    cropped = cropped.rotate(2.9)     # optional rotate and re-crop
#    cropped = cropped.crop((9, 18, 791, 410)) # left, upper, right, lower; image size is 800 x 450 px
    cropped.save(path + "cropped_" + file_root + file_ext, "JPEG")
