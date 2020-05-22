# sudo -H pip3 install Pillow
# after cropping, convert to animated gif with imagemagick:
# convert -delay 10 -loop 0 *.jpg animated.gif
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
    cropped.save(path + "cropped_" + file_root + file_ext, "JPEG")

