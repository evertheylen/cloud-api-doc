import requests

from ef_auth import ef_authheaders

###
### API Call is GET /tags - list all tags for user
###

url = 'https://api.eyefi.com/3/tags'
response = requests.get(url, headers=ef_authheaders())

###
### Retrieve response, parse JSON, loop through results
###

if (response.status_code == 200):
    tags = response.json()

    print response.json()

    for tag in tags:
        print str(tag['id']) + ' ' + tag['name']

else:
    print "An error occurred"
    print response.url
    print response.status_code
    print response.text
