import requests

from ef_auth import ef_authheaders

###
### API Call is GET /albums/:id - Get the album information
###         and PUT /albums/:id - Update album information (sucha s name)
###

###
### First get all albums looking for 'New Album' for a user so we have an object to work with
###
### A good sequence to run this example is to do albums_post.py first
### This will create an album called 'New Album' for testing purposes.
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
        response = requests.get(url, headers=ef_authheaders())

        if (response.status_code == 200):
            url = 'https://api.eyefi.com/3/albums' + '/' + str(selected_album)
            newalbumname = { 'name' : 'New New Album' }
            response = requests.put(url, json=newalbumname, headers=ef_authheaders())

            if (response.status_code == 200):
                print 'Successfully renamed album'
                
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


else:
    print "An error occurred"
    print response.url
    print response.status_code
    print response.text

