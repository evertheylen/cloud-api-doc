import requests
import json

from StringIO import StringIO

from PIL import Image

from ef_auth import ef_authheaders

###
### API Call is GET /tags/:id/files - get all files with a tag.
###
### Use this to download all files with a tag
###

###
### First search all the user's tags for the 'APITestTag' tag so we have an object to work with
###
### A good sequence to run this example is to do files_id_tags_post.py first
### This will create a tag called 'APITestTag' and add a file to it to work with
###

url = 'https://api.eyefi.com/3/tags'
response = requests.get(url, headers=ef_authheaders())

if (response.status_code == 200):
    tags = response.json()

    # print response.json()

    ###
    ### Select the album with the title 'New Album' (created with the albums_post example)
    ###

    for tag in tags:
        if (tag['name'] == 'APITestTag'):
            selected_tag = tag['id']

###
### Now get the photos in the album
###

url = 'https://api.eyefi.com/3/tags' + '/' + str(selected_tag) + '/' + 'files'
response = requests.get(url, headers=ef_authheaders())

if (response.status_code == 200):
    files = response.json()

    # print files

    ###
    ### Download the files
    ###

    for fileitem in files:
        filename = fileitem['name']
        url = fileitem['media']

        ###
        ### In this example, the Python Image Library (PIL) object is used to save the file to disk
        ###

        response = requests.get(url, headers=ef_authheaders())

        if (response.status_code == 200):
            im = Image.open(StringIO(response.content))
            im.save(filename)

            print 'Successfully downloaded ' + filename
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

