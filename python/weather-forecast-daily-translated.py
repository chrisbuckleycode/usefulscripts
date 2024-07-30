## FILE: weather-forecast-daily-translated.py
##
## DESCRIPTION: Scrapes a desired section of text from a web site.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: python3 weather-forecast-daily-translated.py
##
# TODO(chrisbuckleycode): Add translation function.

# from bs4 import BeautifulSoup
import urllib.request
import re


uri = 'https://www.knmi.nl/nederland-nu/weer/verwachtingen'

htmlBlock = urllib.request.urlopen(uri).read()

soup = BeautifulSoup(htmlBlock, 'html.parser')

#[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
# extract only what needed i.e. document
[s.extract() for s in soup(['[document]'])]

visible_text = soup.getText()

try:
    wantedSection = re.search('Waarschuwingen(.+?)\(Bron', visible_text).group(0)
    print(wantedSection)
except AttributeError:
    print('wantedSection not found')

# Translation to follow
