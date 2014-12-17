import requests
import json

from ef_auth import ef_authheaders

###
### API Call is GET /albums/:id/files - get all files in an album
###         and PUT /albums/:id/files - replace all files in an album
###
### Use this to reverse the order of a set of photos in an album
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
### Now get the photos in the album
###

url = 'https://api.eyefi.com/3/albums' + '/' + str(selected_album) + '/' + 'files'
response = requests.get(url, headers=ef_authheaders())

if (response.status_code == 200):
    files = response.json()

    ###
    ### Add the items to filelist and reverse it
    ###

    filelist = []
    i = 0
    for fileitem in files:
        filelist.append( { 'id' : files[i]['id'] } )
        i += 1

    filelist.reverse()

    ###
    ### Now put those back to the existing album
    ###

    url = 'https://api.eyefi.com/3/albums' + '/' + str(selected_album) + '/' + 'files'
    headers = ef_authheaders()
    response = requests.put(url, json=filelist, headers=headers)

    ###
    ### Retrieve response, parse JSON, display results
    ### PUT and POST requests can return 200 or 201 on success
    ###

    if (response.status_code == 200 or response.status_code == 201):
        print 'Successfully added files to album'
    else:
        print "An error occurred"
        print response.url
        print response.status_code
        print response.text

