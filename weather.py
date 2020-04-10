# weather
# this script scrapes weather forecast data from a popular site. The url has been obfuscated so this script is for educational value only.
# I took inspiration from this nice tutorial here: https://medium.com/@aakankshaws/using-beautifulsoup-requests-to-scrape-weather-data-9c6e9d317800
# by https://www.linkedin.com/in/aakankshaws/
# This script uses the requests module but would be better replaced in future with urllib3 module and using a custom user-agent instead.

import webbrowser



import requests
page = requests.get("https://worldweathertoday.com/en-US/worldweathertoday/tenday/l/NLXX0002:1:NL")

from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,"html.parser")

all=soup.find("div",{"class":"locations-title ten-day-page-title"}).find("h1").text
table=soup.find_all("table",{"class":"twc-table"})
degree_sign= u'\N{DEGREE SIGN}'
l=[]
for items in table:
# for i in range(len(items.find_all("tr"))-1):
 for i in range(0,5):
  d = {}
  d["Day"]=items.find_all("span",{"class":"date-time"})[i].text
  d["Date"]=items.find_all("span",{"class":"day-detail"})[i].text
  d["Description"]=items.find_all("td",{"class":"description"})[i].text
  # d["Temperature (High/Low) F"]=items.find_all("td",{"class":"temp"})[i].text
  tempfahr = items.find_all("td",{"class":"temp"})[i].text
  try:
   tempfmax = float(tempfahr[0:2])
   tempcmax = (5 / 9)*(tempfmax - 32)
   tempfmin = float(tempfahr[3:5])
   tempcmin = (5 / 9) * (tempfmin - 32)
   d["Temperature (High/Low) C"] = "{:.0f}".format(tempcmax) + degree_sign + " / " + "{:.0f}".format(tempcmin) + degree_sign
  except ValueError:
   tempcmax = tempfahr[0:2]
   tempfmin = float(tempfahr[2:4])
   tempcmin = (5 / 9) * (tempfmin - 32)
   d["Temperature (High/Low) C"] = tempcmax + " / " + "{:.0f}".format(tempcmin) + degree_sign
#  tempfmax = float(tempfahr[0:2])
#  tempfmin = float(tempfahr[3:5])
#  tempcmax = (5/9)*(tempfmax - 32)


  d["Precip."]=items.find_all("td",{"class":"precip"})[i].text
  d["Wind"]=items.find_all("td",{"class":"wind"})[i].text
  d["Humidity"]=items.find_all("td",{"class":"humidity"})[i].text
  l.append(d)

print(l)

import pandas
df = pandas.DataFrame(l)
# df = df.drop(df.columns[[0]], axis=1)

# df.set_index('Date', inplace=True)
# df = df.rename_axis(None)

# print(df)
# print(df.iloc[[0]])


html = df.to_html(index = False)
# html = df.iloc[[0]].to_html()


# print(html)

filename = "demofile4.html"
f = open(filename, "w")
# f.write("<html><head></head><html>")
# f.write("<p>blabla</p>")
# f.write("</body></html>\n")
print("<html><head></head><html>", file=f)
print("<p>Today's weather in Amsterdam</p>", file=f)
print(html, file=f)
print("</body></html>", file=f)
f.close()

#open and read the file after the appending:
f = open(filename, "r")
print(f.read())




webbrowser.open(
    filename
)
