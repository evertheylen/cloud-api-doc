import requests

from ef_auth import ef_authheaders

###
### API Call is GET /albums - list all albums for user
###

url = 'https://api.eyefi.com/3/albums'
response = requests.get(url, headers=ef_authheaders())

###
### Retrieve response, parse JSON, loop through results
###

if (response.status_code == 200):
    albums = response.json()

    # print response.json()

    for album in albums:
        print str(album['id']) + ' ' + album['name']

else:
    print "An error occurred"
    print response.url
    print response.status_code
    print response.text
