## FILE: randompic.py
##
## DESCRIPTION: Displays random pic from a directory.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: python3 randompic.py
##

# # display random picture from ./quotes/ directory
# this script will create and then display and html file composed of a single random image plucked from a sub-directory called "quotes".

import sys
import webbrowser
import random
import os

path = "./quotes/"

files = os.listdir(path)
random_image_filename = random.choice(files)

filename = "index.htm"
f = open(filename, "w")

print("<html><head></head><html>", file=f)
print("<p>Random Image</p>", file=f)
print("<img src=\"" + path + random_image_filename + "\">", file=f)
print("</body></html>", file=f)
f.close()

#open and read the file after the appending:
f = open(filename, "r")
print(f.read())

webbrowser.open(
    filename
)

sys.exit(0)
