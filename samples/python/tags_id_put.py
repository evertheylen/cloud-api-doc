import requests
import json

from ef_auth import ef_authheaders

###
### API Call is PUT /tags/:id - rename a tag
###

###
### First get all tags looking for 'APITestTag' for a user so we have an object to work with
###
### A good sequence to run this example is to run files_id_tags_post.py first
### This will create an tag called 'APITestTag' for testing purposes.
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
        if (tag['name'] == 'APITestTag'):
            selected_tag = tag['id']

    ###
    ### Rename the tag to 'APITestTagDemo'
    ###

    data = { 'name' : 'APITestTagDemo'}

    url = 'https://api.eyefi.com/3/tags' + '/' + str(selected_tag)
    headers = ef_authheaders()
    response = requests.put(url, json=data, headers=headers)

    ###
    ### Retrieve response, parse JSON, display results
    ### PUT and POST requests typically return 201 on success
    ###

    if (response.status_code == 201):
        print 'Successfully renamed tag'
    else:
        print "An error occurred"
        print response.url
        print response.status_code
        print response.text

