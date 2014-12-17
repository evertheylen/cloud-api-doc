from PIL import Image
from PIL import ImageOps
from StringIO import StringIO
import requests
import json

from ef_auth import ef_authheaders

###
### API Call is POST /search/saved - create a saved search
###
### An additional call will be made to the Google maps API to get the lat and long of "My Location".
### This will be added as a filter to an album query.  This is best run after albums_post.py and
### albums_id_files_post.py to create the 'New Album' album and populate it with files.
###

###
### This URL refers to Eye-Fi headquarters.  Use an address near where you took the pictures in your
### photo collection that have been added to the 'New Album' album.
###

### url = 'https://maps.googleapis.com/maps/api/geocode/json?address=927+N.+Shoreline+Blvd.,+Mountain+View,+CA'
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=Disneyland'
response = requests.get(url)
result = response.json()['results'][0]

lat_param = result['geometry']['location']['lat']
lon_param = result['geometry']['location']['lng']

###
### Create query criteria
###

url = 'https://api.eyefi.com/3/search/saved'
data = { 'name': 'APITestSavedSearch',
         'query': {
                  'has_geodata': True, 'geo_lat': lat_param, 'geo_lon': lon_param, 'geo_distance': '5mi'
                  }
       }

### TODO add album id search id here

response = requests.post(url, json=data, headers=ef_authheaders())

if (response.status_code == 201):
    savedsearch = response.json()

    ###
    ### Now execute the saved search and list the files
    ###

    url = 'https://api.eyefi.com/3/search/saved' + '/' + str(savedsearch['id']) + '/' + 'files'
    response = requests.get(url, headers=ef_authheaders())

    if (response.status_code == 200):
        fileitems = response.json()['items']

        for fileitem in fileitems:
            print str(fileitem['id']) + ' ' + fileitem['name']

    else:
        print "An error occurred"
        print response.url
        print response.status_code
        print response.text

else:
    print "An error occurred"
    print response.url
    print response.status_code
    print response.text

