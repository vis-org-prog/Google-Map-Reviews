#importing libraries
import urllib.parse
import requests
import pprint # it will print in a good format
import json
 
 #initializing key which is made constant
KEY = "AIzaSyBN3tEFPa739-NgoHudL929dbvc2uhwP_4"



#function that can be used in python which is geocde place and it receives place and returns the geocode with place 
#and we have url 
#geocoding ?  - we send the name of the place in the google maps so the geocode api returns place id which is primary key which is a special table 
#in a database.  So the output may be in json format or xml
#json? - its like how to format the data. Json is mix of keys and values
#then we have 2 param address the place we are looking for and key is the google map
def geoCodePlace(place):
    """Returns the geoCodedPlace for the given place"""
 
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": place, "key": KEY}
    response = requests.get(url, params=urllib.parse.urlencode(params))
    return response.json()


def getPlaceDetails(place_id):
    """Returns the place details for the given place id"""

    url = "https://places.googleapis.com/v1/places/{}".format(place_id)
    params = {
        "fields": "id,displayName,rating,userRatingCount,reviews",
        "key": KEY,
    }
    response = requests.get(url, params=urllib.parse.urlencode(params))
    return response.json()


def main():
    # Define the place
    place = "Flavours of India, Kingston"

    # Get the geoCodedPlace
    geoCodedPlace = geoCodePlace(place)
    print("\nThis is the geoCodedPlace:")
    pprint.pprint(geoCodedPlace)


    # Get the place id
    place_id = geoCodedPlace["results"][0]["place_id"]
    print("\nThis is the place id:")
    print(place_id)


    # Get the place details
    placeDetails = getPlaceDetails(place_id)
    print("\nThese are the place details:")
    pprint.pprint(placeDetails)

#optional step


if __name__ == "__main__":
    main()
    

