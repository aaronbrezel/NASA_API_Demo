##NASA API Demo

from NASA_API_Credentials import api_key
import requests

##base url. Every http request to the Rover API will start with this string
base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/"


def api_Request():
    return "Hello World"




request_url = "{}Curiosity/photos?sol=900&api_key={}".format(base_url,api_key)

#print(request_url)


test_request = requests.get(request_url)

test_data = test_request.json()


#print(test_data['photos'][0]['camera']['id'])