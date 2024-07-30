from bs4 import BeautifulSoup
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
