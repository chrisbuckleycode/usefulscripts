#!/usr/bin/env python

from geopy.geocoders import Nominatim
import webbrowser

def get_coordinates(location):
    geolocator = Nominatim(user_agent="my-app")  # Provide a custom user agent

    # Geocode the given location
    location_data = geolocator.geocode(location)

    if location_data:
        # Extract the latitude and longitude from the location data
        lat = location_data.latitude
        lng = location_data.longitude
        return lat, lng

    return None

def geohack_url(coords):
    url = f"https://geohack.toolforge.org/geohack.php?language=en&params={coords[0]};{coords[1]}"
    return url


# Prompt the user for a location
location = input("Enter a location: ")

# Get the coordinates
coordinates = get_coordinates(location)

if coordinates:
    print("Coordinates: {}, {}".format(coordinates[0], coordinates[1]))
else:
    print("Unable to find coordinates for the given location.")

# Get the url
url = geohack_url(coordinates)
print(f"Url: {url}")

webbrowser.open(url)
