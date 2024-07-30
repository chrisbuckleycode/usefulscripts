## FILE: bmarks-sort-alpha-title-only.py
##
## DESCRIPTION: Sorts bookmarks alphabetically. Displays Title only.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: python3 bmarks-sort-alpha-title-only.py
##

from bs4 import BeautifulSoup
import os

# Open and read the HTML file
with open("bookmarks.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# Create a dictionary where the key is the title and the value is the corresponding URL
bookmarks = {}
for link in soup.find_all("a"):
    bookmarks[link.get_text()] = link["href"]

# Sort the dictionary by value (URL) in alphabetical order
sorted_bookmarks = dict(sorted(bookmarks.items(), key=lambda item: item[1]))

# Create and save an HTML page with a list of hyperlinks
with open("sorted_bookmarks.html", "w") as file:
    file.write("<html><body>")
    for title, url in sorted_bookmarks.items():
        file.write(f"<a href='{url}'>{title}</a><br>\n")
    file.write("</body></html>")
