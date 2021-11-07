import dotenv
import requests
import os
from dotenv import load_dotenv, find_dotenv
import urllib.parse
import place_request

def get_road_name(latitude, longitude):
    load_dotenv(find_dotenv())
    point = latitude + "," + longitude

    # Get the placeId of current location
    # Complete the url
    url = "https://roads.googleapis.com/v1/nearestRoads?points="
    key = "&key=" + os.getenv('GOOGLE_API_KEY')
    
    # complete and encode url
    url += urllib.parse.quote(point) + key

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    arr = response.json()["snappedPoints"]

    placeId = arr[0]["placeId"]

    # Get the road name from placeID
    return place_request.place_request(placeId)

# get_road_name("40.00372338521878,-83.01264987638984")