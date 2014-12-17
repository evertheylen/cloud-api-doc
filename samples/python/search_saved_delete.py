from PIL import Image
from PIL import ImageOps
from StringIO import StringIO
import requests
import json

from ef_auth import ef_authheaders

###
### API Call is DELETE /search/saved/:id - Delete specified saved search
###

url = 'https://api.eyefi.com/3/search/saved'
response = requests.get(url, headers=ef_authheaders())

if (response.status_code == 200):
    searches = response.json()

    selected_savedsearch = 0
    for searchitem in searches:
        if searchitem['name'] == 'APITestSavedSearch':
            selected_savedsearch = searchitem['id']

    url = 'https://api.eyefi.com/3/search/saved' + '/' + str(selected_savedsearch)
    response = requests.delete(url, headers=ef_authheaders())

    if (response.status_code == 204):
        searches = response.json()

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

