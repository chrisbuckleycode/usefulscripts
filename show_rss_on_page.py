# This script displays RSS feeds in a new html page.
# Put RSS urls in rss_urls.txt


import feedparser
import webbrowser


def show_feed(feedurl, article_count):

    d = feedparser.parse(feedurl)

    feed_title = d.feed.title
    feed_url = d.feed.title_detail.base

    print("<p><h2>" + feed_title + "</h2></p>", file=f)
    print("<p>" + feed_url + "</p>", file=f)
    # print('RSS Feed Title is: ' + '\n' + feed_title + '\n', file=f)
    # print('RSS Feed url is: ' + '\n' + feed_url + '\n', file=f)

    # limit = len(d.entries)
    # print('Limit is: ' + '\n' + str(limit) + '\n')


    # for i in range(0, limit):
    for i in range(0, article_count):
        item = d.entries[i]
        item_name = item.title[:100]
        item_link = item.link
        # print(item_name + '\n')
        # print(item_link + '\n' + '\n')
        print("<p>" + str(i + 1) + ") <a target='_blank' href='" + item_link + "'>" + item_name + "</a></p>", file=f)
    print("<p>~ ~ ~ ~</p>", file=f)
        

filename = "index.htm"
f = open(filename, "w")
    
print("<html><head></head><html>", file=f)
print("<p><h1>RSS Feeds</h1></p>", file=f)


###### BEGIN RSS FEEDS ######

# show_feed('https://www.reddit.com/r/Coronavirus.rss', 5)
# show_feed('https://www.reddit.com/r/Coronavirus/rising.rss', 5)

g = open(r"rss_urls.txt", "r")

# Initialize list.
lines = []

# Convert into strings
for line in g.readlines():
    li = line.rstrip()
    if not li.startswith("#"):
        lines.append(li)
    

for each_url in lines:
    show_feed(each_url, 5)

g.close()
###### END RSS FEEDS ######

    
print("</body></html>", file=f)
f.close()

# open and read the file after the appending:
# f = open(filename, "r")
# print(f.read())

webbrowser.open(
    filename
)
