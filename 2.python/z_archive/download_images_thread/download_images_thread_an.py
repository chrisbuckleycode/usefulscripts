## FILE: download_images_thread_an.py
##
## DESCRIPTION: Downloads images from sub-page of a popular site.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: python3 download_images_thread_an.py
##

# TODO(chrisbuckleycode): Reword/refactor below comment
# This script will download images from a sub-page of a popular site. As I won't reveal that, this script is for educational value only. You must modify the 'url' and 'user_agent' variables. You can get a random user agent from here: https://user-agents.net/random


from bs4 import BeautifulSoup
import urllib3
import wget

user_agent = {Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17}

http = urllib3.PoolManager(10, headers=user_agent)

r = http.urlopen('GET', 'https://whatever.com/whatever-page')

soup = BeautifulSoup(r.data)

images = []

for link in soup.findAll('a', {'class': 'fileThumb'}):
    try:
        wget.download('https:'+link['href'])
    except KeyError:
        pass
