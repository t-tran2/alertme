import dotenv
import requests
import os
from dotenv import load_dotenv, find_dotenv
import urllib.parse
# This function sends a request to the places api for the road name
# @param placeId
# The placeId
def place_request(placeId):
    load_dotenv(find_dotenv())

    # Get the placeId of current location
    # Complete the url
    url = "https://maps.googleapis.com/maps/api/place/details/json?place_id="
    key = "&key=" + os.getenv('GOOGLE_API_KEY')
    
    # complete and encode url
    url += placeId + "&fields=address_components" +  key

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    arr = response.json()["result"]["address_components"]

    i = 0
    while i < len(arr) and arr[i]["types"][0] != "route":
        i+= 1
    if i == len(arr):
        return "No route"

    # split strings
    long_name = arr[i]["long_name"]
    short_name = arr[i]["short_name"]
    long_name_arr = long_name.split()
    short_name_arr = short_name.split()
    long_cut = long_name
    short_cut = short_name
    if len(long_name_arr) > 1 :
        long_name_arr = long_name_arr[:-1]
        long_cut = " ".join(long_name_arr)
    if len(short_name_arr) > 1 :
        short_name_arr = short_name_arr[:-1]
        short_cut = " ".join(short_name_arr)
    ret_value = [long_name,short_name,long_cut,short_cut]

    return ret_value

# Print test of place_request()
#place_request("ChIJ7Tl4B72OOIgRcHA3ssKPmiY")