#!/usr/bin/env python

# sudo -H pip3 install mistletoe

import webbrowser
import mistletoe
from bs4 import BeautifulSoup

with open('accesstoken.txt', 'r') as markdown_file:

    access_token = str(markdown_file.readlines(1))
    access_token = access_token[2:-4]
    
markdown_file.close()

# access_token = "XXX"

# author_name = "John Doe"

# author_url = "https://google.com"

# title = "Sample Page"

# content = ""



with open('markdown.txt', 'r') as file_headers:

    title = str(file_headers.readlines(1))
    author_name = str(file_headers.readlines(2))
    author_url = str(file_headers.readlines(3))
    image_url = str(file_headers.readlines(4))

file_headers.close()

title_cleaned = title[2:-4]
author_name_cleaned = author_name[2:-4]
author_url_cleaned = author_url[2:-4]
image_url_cleaned = image_url[2:-4]

title_chopped = title_cleaned.split(' ', 1)[1]
author_name_chopped = author_name_cleaned.split(' ', 1)[1]
author_url_chopped = author_url_cleaned.split(' ', 1)[1]
image_url_chopped = image_url_cleaned.split(' ', 1)[1]

# print (title_chopped)
# print (author_name_chopped)
# print (author_url_chopped)
# print (image_url_chopped)

# input("Press Enter to continue...")



with open('markdown.txt', 'r') as file_contents:
#default:    rendered = mistletoe.markdown(file_contents)
    contents_rendered = mistletoe.markdown(file_contents.readlines()[6:])
file_contents.close()
# print (contents_rendered)    


    
# input("Press Enter to continue...")


filename = "index.htm"
f = open(filename, "w")

print("<html><head></head><html>", file=f)

print("<h1>Telegra.ph</h1>", file=f)

print("<h1>Metadata</h1>", file=f)

if access_token:
    print("<p>Access Token is: <b>populated</b></p>", file=f)
else:
    print("<p>Access Token is: <b>NOT</b> populated!</p>", file=f)
if author_name:
    print("<p>Author Name: <b>" + author_name_chopped + "</b></p>", file=f)
else:
    print("<p>Author Name: <b>NOT</b> populated!</p>", file=f)
if author_url:
    print("<p>Author url: <b>" + author_url_chopped + "</b></p>", file=f)
else:
    print("<p>Author url: <b>NOT</b> populated!</p>", file=f)
if image_url:
    print("<p>Image url: <b>" + image_url_chopped + "</b></p>", file=f)

    
print("<br />", file=f)    
    
info_url = "https://api.telegra.ph/getAccountInfo?access_token=" + access_token + "&fields=[%22short_name%22,%22author_name%22,%22author_url%22,%22auth_url%22,%22page_count%22]"

print("<a target=\"_blank\" href=\"" + info_url + "\">Get Account Info</a>", file=f)

info_url = "https://api.telegra.ph/getPageList?access_token=" + access_token + "&limit=200"

print("<a target=\"_blank\" href=\"" + info_url + "\">Get Page List</a>", file=f)



print("<br />", file=f)    
print("<br />", file=f)  

if title:
    print("<p>Post Title: <b>" + title_chopped + "</b></p>", file=f)
else:
    print("<p>Post Title: <b>NOT</b> populated!</p>", file=f)


print("<h2>Post Body</h2>", file=f)

if image_url:
    print("<p><img src=\"" + image_url_chopped + "\"></p>", file=f)


print (contents_rendered, file=f)

print("<p>End of Preview</p>", file=f)
print("<p>~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>", file=f)

new_title = title_chopped.replace(" ", "+")
# input("Press Enter to continue...")


#https://api.telegra.ph/createPage?access_token=XXX&author_name=XXX&author_url=XXX&title=XXX&content=[{"tag":"p","children":["test!"]},{"tag":"p","children":["a,+b!"]},{"tag":"img","attrs":{"src":"https://i.redd.it/1phq9yjz2jx41.jpg"}}]&return_content=true

# {"tag":"p","children":["        a,+b!              "]}
# {"tag":"p","children":["a,+b!"]}

lhs = "%7B%22tag%22%3A%22p%22%2C%22children%22%3A%5B%22"
rhs = "%22%5D%7D"
# separate words with "+" except end

page_content = BeautifulSoup(contents_rendered,'html.parser')
result = page_content.find_all("p")

#print(result, file=f)

result_stringed = str(result)

# print(result_stringed, file=f)

# print("<p>~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>", file=f)

result_stringed = result_stringed.replace("<p>", lhs)
result_stringed = result_stringed.replace("</p>", rhs)
result_stringed = result_stringed.replace("%7D, %7B", "%7D,%7B")
result_stringed = result_stringed.replace(" ", "+")

# print(result_stringed, file=f)


create_url = "https://api.telegra.ph/createPage?access_token=" + access_token + "&author_name=" + author_name_chopped + "&author_url=" + author_url_chopped + "&title=" + new_title + "&content=" + result_stringed + "&return_content=true"

# {"tag":"img","attrs":{"src":"https:bla.com/image.jpg"}}
if image_url:
    image_lhs = "%7B%22tag%22%3A%22img%22%2C%22attrs%22%3A%7B%22src%22%3A%22"
    image_rhs = "%22%7D%7D%2C"
    element_to_insert = image_lhs + image_url_chopped + image_rhs
    create_url = "https://api.telegra.ph/createPage?access_token=" + access_token + "&author_name=" + author_name_chopped + "&author_url=" + author_url_chopped + "&title=" + new_title + "&content=" + result_stringed[:1] + element_to_insert + result_stringed[1:] + "&return_content=true"
    

print("<a target=\"_blank\" href=\"" + create_url + "\">Create Post</a>", file=f)




print("</body></html>", file=f)
f.close()

#open and read the file after the appending:
ff = open(filename, "r")
print(ff.read())

webbrowser.open(
    filename
)
ff.close()
