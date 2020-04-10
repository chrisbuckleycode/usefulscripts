# This script will download images from a sub-page of a popular site. As I won't reveal that, this script is for educational value only. You must modify the 'url' and 'user_agent' variables. You can get a random user agent from here: https://user-agents.net/random

from bs4 import BeautifulSoup
import urllib3
# import re, requests
import wget

url = 'https://whatever.com/whatever-page'

user_agent = {Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17}

http = urllib3.PoolManager(10, headers=user_agent)

r = http.urlopen('GET', url)

# print(r.data)


# r = http.request('GET', url)
# r.headers

soup = BeautifulSoup(r.data)

# print(soup)

images = []
# for img in soup.findAll('img'):
#    images.append(img.get('src'))
# for img in soup.findAll("a", {"class":"fileThumb"}):
#     print (img['src'])
# images = soup.findAll('href')

# this will return src attrib from img tag that is inside 'a' tag


for link in soup.findAll('a', {'class': 'thread_image_link'}):
    try:
#        print ('https:'+link['href'])
        wget.download(link['href'])
    except KeyError:
        pass
    


# wget.download('')
    
    # link.attrs['href']

# type(link)
