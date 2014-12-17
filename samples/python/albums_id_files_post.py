import requests
import json

from ef_auth import ef_authheaders

###
### API Call is POST /albums/:id/files - add files to an existing album identified by id :id
###

###
### First search all the user's albums for the 'New Album' album so we have an object to work with
###
### A good sequence to run this example is to do albums_post.py first
### This will create an album called 'New Album' that we can add files to
###

url = 'https://api.eyefi.com/3/albums'
response = requests.get(url, headers=ef_authheaders())

if (response.status_code == 200):
    albums = response.json()

    # print response.json()

    ###
    ### Select the album with the title 'New Album' (created with the albums_post example)
    ###

    for album in albums:
        if (album['name'] == 'New Album'):
            selected_album = album['id']

###
### Now grab 3 files to add to the album.  For convenience pick the first 3 returned by the GET /files API
###

url = 'https://api.eyefi.com/3/files'
response = requests.get(url, headers=ef_authheaders())


if (response.status_code == 200):
    files = response.json()

    filelist = []
    if (files['total_count'] < 3):
        print 'Please add some files to your account.'
        exit(-1)
    else:
        ###
        ### Add the first 3 items as dicts keyed off of 'id' to the file list
        ###

        filelist.append( { 'id' : files['items'][0]['id'] } )
        filelist.append( { 'id' : files['items'][1]['id'] } )
        filelist.append( { 'id' : files['items'][2]['id'] } )

        ###
        ### Now add those files to the 'New Album' album
        ###
        ### There is a trick here to get the filelist array encoded successfully for requests.  Normally
        ### requests will serialize a dictionary passed to it's data parameter.  Since the filelist is a simple
        ### list it's much easier to pass it to the request using the json parameter.  This is equivalent to
        ### setting data to json.dumps(filelist) and adding a content-type header for application/json.
        ###

        url = 'https://api.eyefi.com/3/albums' + '/' + str(selected_album) + '/' + 'files'
        headers = ef_authheaders()
        response = requests.post(url, json=filelist, headers=headers)

        ###
        ### Retrieve response, parse JSON, display results
        ### PUT and POST requests typically return 201 on success
        ###

        if (response.status_code == 201):
            print 'Successfully added files to album'
        else:
            print "An error occurred"
            print response.url
            print response.status_code
            print response.text

