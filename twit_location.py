#!/usr/bin/env python

import requests
import json

city = input("Enter city name: ")

# Pass city name to nominatim API
# This is a free API requiring no key
url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
response = requests.get(url)
data = json.loads(response.text)

# Extract latitude and longitude from API response
latitude = data[0]["lat"]
longitude = data[0]["lon"]

# Create Twitter search URL with latitude, longitude and 5 mile radius
radius = 5
twitter_url = f"https://twitter.com/search?q=geocode:{latitude},{longitude},{radius}mi"

print("Twitter search URL:", twitter_url)
