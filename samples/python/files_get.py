from PIL import Image
from PIL import ImageOps
from StringIO import StringIO
import requests
import json

from ef_auth import ef_authheaders

###
### API Call is GET /files - list files associated with a users account
###
### This will then be used to download the first file in the list
###

url = 'https://api.eyefi.com/3/files'
response = requests.get(url, headers=ef_authheaders())

if (response.status_code == 200):
    files = response.json()

    ###
    ### Download the first file
    ###
    ### The attribute 'media' in an individual file object contains a fully assembled
    ### url that can be used to download the original sized image
    ###

    url = files['items'][0]['media']
    response = requests.get(url, headers=ef_authheaders())

    ###
    ### In this example, the Python Image Library (PIL) object is used to convert the image to greyscale
    ### and save it to disk
    ###

    im = Image.open(StringIO(response.content))
    im_grayscale = ImageOps.grayscale(im)
    im_grayscale.save('thefile.jpg')

else:
    print "An error occurred"
    print response.url
    print response.status_code
    print response.text

