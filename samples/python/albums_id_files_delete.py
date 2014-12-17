import requests
import json

from ef_auth import ef_authheaders

###
### API Call is DELETE /albums/:id/files/:fileid - delete the selected file from an album
###
### Use this to delete the first photo in an album
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
    ### Delete the first photo
    ###

    url = 'https://api.eyefi.com/3/albums' + '/' + str(selected_album) + '/' + 'files' + '/' + str(files[0]['id'])
    headers = ef_authheaders()
    response = requests.delete(url, headers=headers)

    ###
    ### Retrieve response, parse JSON, display results
    ### DELETE requests usually return 204
    ###

    if (response.status_code == 204):
        print 'Successfully added files to album'
    else:
        print "An error occurred"
        print response.url
        print response.status_code
        print response.text
