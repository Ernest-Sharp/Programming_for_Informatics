# The program will prompt for a location, contact a web
# service and retrieve JSON for the web service and parse
# that data, and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies
#  a place as within Google Maps.

import urllib
import json

endpoint = "http://python-data.dr-chuck.net/geojson?"

address = raw_input("Enter location: ")
url = endpoint + urllib.urlencode({'sensor':'false', 'address': address})

urlhandler = urllib.urlopen(url).read()
data = json.loads(urlhandler)

print "Retrieving URL: ", url
print "Retrieved ", len(urlhandler), "characters"
print "Place id", data['results'][0]['place_id']