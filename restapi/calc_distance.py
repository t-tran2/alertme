
# Python 3 program to calculate Distance Between Two Points on Earth
from math import radians, cos, sin, asin, sqrt

"""Haversine formula to calculate distance between to coordinates"""
def calc_distance(lat1, lon1, lat2, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(float(lon1))
    lon2 = radians(lon2)
    lat1 = radians(float(lat1))
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in miles. Use 3956 for miles
    r = 3956
      
    # calculate the result
    return(c * r)