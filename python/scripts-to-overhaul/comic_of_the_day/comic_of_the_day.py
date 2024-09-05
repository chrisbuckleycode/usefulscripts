## FILE: comic_of_the_day.py
##
## DESCRIPTION: Displays comic of the day.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: python3 comic_of_the_day.py
##

# this script takes the comic of the day (an image) from a particular web site, downloads it and creates an HTML page to display it. It uses the first image found of a specified class. User agent should be changed for your own use e.g.use https://user-agents.net/random


from datetime import datetime
import webbrowser
from bs4 import BeautifulSoup
import urllib3
# import re, requests
import wget


user_agent = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; HTC Desire 530 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36'}

http = urllib3.PoolManager(10, headers=user_agent)

theurl = 'https://BLABLABLABLABLA.com/'

r = http.urlopen('GET', theurl)

soup = BeautifulSoup(r.data, features="html.parser")

images = soup.findAll('img', {'class': 'img-responsive img-comic'}, limit=1)

for i in images:
    print('https:'+i['src'])

todaysimageurl = 'https:'+i['src']
print(todaysimageurl)

wget.download(todaysimageurl)

imagefilename = "dt" + datetime.today().strftime('%y%m%d') + ".gif"

filename = "index.htm"
f = open(filename, "w")

print("<html><head></head><html>", file=f)
print("<p>Today's Cartoon</p>", file=f)
print("<img src=\"" + imagefilename + "\">", file=f)
print("</body></html>", file=f)
f.close()

#open and read the file after the appending:
f = open(filename, "r")
print(f.read())

webbrowser.open(
    filename
)
