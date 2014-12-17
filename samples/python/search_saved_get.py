from PIL import Image
from PIL import ImageOps
from StringIO import StringIO
import requests
import json

from ef_auth import ef_authheaders

###
### API Call is GET /search/saved - list saved searches in a users account
###

url = 'https://api.eyefi.com/3/search/saved'
response = requests.get(url, headers=ef_authheaders())

if (response.status_code == 200):
    searchitems = response.json()

    for searchitem in searchitems:
        print str(searchitem['id']) + ' ' + searchitem['name']
        print searchitem['query']
        print

else:
    print "An error occurred"
    print response.url
    print response.status_code
    print response.text

