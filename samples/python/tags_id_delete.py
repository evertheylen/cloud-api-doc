import requests
import json

from ef_auth import ef_authheaders

###
### API Call is DELETE /tags/:id - delete a tag
###

###
### First get all tags looking for 'APITestTagDemo' for a user so we have an object to work with
###
### A good sequence to run this example is to run files_id_tags_post.py first and then run tags_id_put.py
### This will create an tag called 'APITestTagDemo' for testing purposes.
###

url = 'https://api.eyefi.com/3/tags'
response = requests.get(url, headers=ef_authheaders())

if (response.status_code == 200):
    tags = response.json()

    # print response.json()

    ###
    ### Select the tag  with the title 'APITestTag (created with the files_id_tags_post example)
    ###

    for tag in tags:
        if (tag['name'] == 'APITestTagDemo'):
            selected_tag = tag['id']

    ###
    ### Delete the tag
    ###

    url = 'https://api.eyefi.com/3/tags' + '/' + str(selected_tag)
    headers = ef_authheaders()
    response = requests.delete(url, headers=headers)

    ###
    ### Retrieve response, parse JSON, display results
    ### PUT and POST requests typically return 201 on success
    ###

    if (response.status_code == 204):
        print 'Successfully deleted tag'
    else:
        print "An error occurred"
        print response.url
        print response.status_code
        print response.text

