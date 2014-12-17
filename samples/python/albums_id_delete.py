import requests

from ef_auth import ef_authheaders

###
### API Call is DELETE /albums/:id - Delete album
###

###
### First get all albums for a user so we have an object to work with
###
### A good sequence to run this example is to do albums_post.py first.
### This will create an album called 'New Album' for testing purposes.
### After it gets deleted by this script, run albums_post.py to create a new version
###

url = 'https://api.eyefi.com/3/albums'
response = requests.get(url, headers=ef_authheaders())

if (response.status_code == 200):
    albums = response.json()

    ###
    ### Select the album with the title 'New Album' (created with the albums_post example) and get it's photos
    ###

    for album in albums:
        if (album['name'] == 'New Album'):
            selected_album = album['id']

    if (selected_album != None):
        url = 'https://api.eyefi.com/3/albums' + '/' + str(selected_album)
        response = requests.delete(url, headers=ef_authheaders())

        if (response.status_code == 204):
            print 'Successfully deleted album'

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


else:
    print "An error occurred"
    print response.url
    print response.status_code
    print response.text

