import json
import base64

###
### Helper function to retrieve Basic Authentication information for a user from a secure location in
### user's home directory.  In this case, the file is called .ef_password in /Users/dave.  The file
### would contain a JSON document that looks like this:
###
###   { "username" : "<username>@<domain>", "password" : "abcdEFGH" }
###
### Add the result of ef_authheaders() to the requests.get/.post call when calling the Eye-Fi API:
###
###   from ef_auth import ef_authheaders
###
###   response = requests.get(url, headers = ef_authheaders()
### 

def ef_authheaders():
    with open('/Users/dave/.ef_password') as auth_file:
        auth_data = json.load(auth_file)
        base64string = base64.encodestring('%s:%s' % (auth_data['username'], auth_data['password'])).replace('\n', '')
        auth_headers = {'Authorization' : 'Basic %s' % base64string}
        return(auth_headers)

