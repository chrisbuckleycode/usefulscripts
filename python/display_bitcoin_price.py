## FILE: display_bitcoin_price.py
##
## DESCRIPTION: Scrapes and displays Bitcoin price.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: python3 display_bitcoin_price.py
##

# TODO(chrisbuckleycode): Reword/refactor below comment
# this script will scrape a particular site for bitcoin price value then save it in an html page and display it. As I won't reveal that site, this script is for educational value only. You must modify the 'url' and 'user_agent' variables. You can get a random user agent from here: https://user-agents.net/random

from datetime import datetime
import webbrowser
from bs4 import BeautifulSoup
import urllib3
# import re, requests
import wget


user_agent = {'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; EZee-Tab96Q10-M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Safari/537.36 [FB_IAB/FB4A;FBAV/158.0.0.38.95;]'}

http = urllib3.PoolManager(10, headers=user_agent)

theurl = 'https://blabla.com/bitcoin-price'

r = http.urlopen('GET', theurl)

soup = BeautifulSoup(r.data, features="html.parser")

price_section = soup.findAll('span', {'class': 'cmc-details-panel-price__price'})

print (str(full_section))

price_section = str(price_section)[1:-1]

print (price_section)

newsoup = BeautifulSoup(price_section)

btc_value = newsoup.get_text()

print (btc_value)



filename = "index.htm"
f = open(filename, "w")

print("<html><head></head><html>", file=f)
print("<p>Live Bitcoin Price</p>", file=f)
print("<p>" + btc_value + " USD</p>", file=f)
print("</body></html>", file=f)
f.close()

#open and read the file after the appending:
f = open(filename, "r")
print(f.read())




webbrowser.open(
    filename
)
