import requests

from ef_auth import ef_authheaders

###
### API Call is GET /tags/:id - Get one tag
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

    # print tags

    ###
    ### Select the tag  with the title 'APITestTag (created with the files_id_tags_post example)
    ###

    for tag in tags:
        if (tag['name'] == 'APITestTag'):
            selected_tag = tag['id']


    url = 'https://api.eyefi.com/3/tags' + '/' + str(selected_tag)
    response = requests.get(url, headers=ef_authheaders())

    ###
    ### Retrieve response, parse JSON, loop through results
    ###

    if (response.status_code == 200):
        tag = response.json()

        # print tag

        print str(tag['id']) + ' ' + tag['name']

    else:
        print "An error occurred"
        print response.url
        print response.status_code
        print response.text
