"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""
from pprint import pprint
import re

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"

FENWAY = "https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """

    f = urllib2.urlopen(url)  # file object
    response_text = f.read()  # str
    response_data = json.loads(response_text)  #dict

    assert isinstance(response_data, dict)
    return response_data

def get_geocode_url(place_name):
    base = 'https://maps.googleapis.com/maps/api/geocode/json?'


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """

    place_name = re.sub(r"\s+", '+', place_name)  #convert whitespace to '+'

    g_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    g_url += place_name

    json = get_json(g_url)

    result = json["results"][0]
    geo_dict = result["geometry"]
    loc_dict = geo_dict["location"]

    lat = loc_dict["lat"]
    long = loc_dict["lng"]

    return lat, long




def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    pass


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    pass


if __name__ == '__main__':
    pprint(get_lat_long('Shoreline Amphitheatre, Mountain View'))
