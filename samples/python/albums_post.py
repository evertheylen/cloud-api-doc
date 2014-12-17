import requests

from ef_auth import ef_authheaders

###
### API Call is POST /albums - create an empty album
###

url = 'https://api.eyefi.com/3/albums'

data = { 'name' : 'New Album' }

response = requests.post(url, data=data, headers=ef_authheaders())

###
### Retrieve response, parse JSON, display results
###

if (response.status_code == 200):
    album = response.json()

    ###
    ### The album id is the key to all further API calls
    ###

    print 'Album ' + str(album['id']) + ' created for "' + album['name'] + '"'

else:
    print "An error occurred"
    print response

