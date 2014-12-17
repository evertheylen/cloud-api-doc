import requests
import json

from ef_auth import ef_authheaders

###
### API Call is POST /files/:id/tags - add a tag to a file (and create the tag if it's not there already)
###

###
### Grab a file to add to the album.  For convenience pick the first one returned by the GET /files API
###

url = 'https://api.eyefi.com/3/files'
response = requests.get(url, headers=ef_authheaders())


if (response.status_code == 200):
    files = response.json()

    ###
    ### Tag the first file with 'APITestTag'
    ###

    data = { 'name' : 'APITestTag'}

    url = 'https://api.eyefi.com/3/files' + '/' + str(files['items'][0]['id']) + '/' + 'tags'
    headers = ef_authheaders()
    response = requests.post(url, json=data, headers=headers)

    ###
    ### Retrieve response, parse JSON, display results
    ### PUT and POST requests typically return 201 on success
    ###

    if (response.status_code == 201):
        print 'Successfully tagged files'
    else:
        print "An error occurred"
        print response.url
        print response.status_code
        print response.text
