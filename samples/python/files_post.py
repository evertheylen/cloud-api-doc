from PIL import Image
from StringIO import StringIO
import requests
import json

from ef_auth import ef_authheaders

###
### API Call is POST /files - upload a file
###
### This example is best run after files_get.py.  The file 'thefile.jpg' will be modified using
### the Python Image Library (PIL) and uploaded
###

url = 'https://api.eyefi.com/3/files'

###
### Get a filehandle for the file and attach it to a 'files' json that will be passed to the
### requests.post call
###

upload_file = open('thefile.jpg','rb')
files = {'file': upload_file}

###
### Add additional metadata (including EXIF) to the file in the data json object.
### When looking in the apps for the file it will be sorted by this date.
###

data = {'date_time_taken' : '2014-11-08T12:00:00+00:00'}

response = requests.post(url, files=files, json=data, headers=ef_authheaders())

###
### Retrieve response, parse JSON, display results
### PUT and POST requests typically return 201 on success
###

if (response.status_code == 201):
    print 'Successfully uploaded file'
else:
    print "An error occurred"
    print response.url
    print response.status_code
    print response.text
            