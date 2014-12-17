from PIL import Image
from PIL import ImageOps
from StringIO import StringIO
import requests
import json

from ef_auth import ef_authheaders

###
### API Call is DELETE /files/:id - delete a file by id
###
### In order to have a complete example a file is downloaded, modified, uploaded, then deleted.
### The response from the upload (POST /files) API call will contain a json object with the file id
### that is used to delete
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
    im_grayscale.save('deletemefile.jpg')

else:
    print "An error occurred"
    print response.url
    print response.status_code
    print response.text

url = 'https://api.eyefi.com/3/files'

###
### Get a filehandle for the file and attach it to a 'files' json that will be passed to the
### requests.post call
###

upload_file = open('deletemefile.jpg','rb')
files = {'file': upload_file}

###
### Add additional metadata (including EXIF) to the file in the data json object
### When looking in the apps for the file it will be sorted by this date.
###

data = {'date_time_taken' : '2014-11-08T12:00:00+00:00'}

response = requests.post(url, files=files, json=data, headers=ef_authheaders())

###
### Retrieve response, parse JSON, display results
### PUT and POST requests typically return 201 on success
###

if (response.status_code == 201):
    fileid = response.json()['id']
    print 'Successfully uploaded file ' + str(fileid)

    url = 'https://api.eyefi.com/3/files' + '/' + str(fileid)
    response = requests.delete(url, headers=ef_authheaders())

    if (response.status_code == 204):
        ###
        ### Retrieve response, parse JSON, display results
        ### PUT and POST requests typically return 201 on success
        ###
        print 'successfully deleted file ' + str(fileid)

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

