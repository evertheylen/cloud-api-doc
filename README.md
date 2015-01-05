# Overview

The Eyefi Cloud API is a RESTful API that uses OAuth 2.0 for authentication.

APIs are provided that allow for Photo upload and download, Album creation and curation, 
Tag creation and curation, and Photo searching.  Eye-Fi will continue to maintain the publicly available API set
through regular updates to the cloud-api-doc GitHub project.

Each API endpoint is described in a separate markdown file.  Parameter descriptions and curl examples are provided
for each API.  Separately there are API code samples provided in Python and there are more extensive
tool examples (Warholizer, Directory Uploader, and Search n' Tag) provided in Python, C#, and JavaScript.
    
Support for the API is provided on a best effort basis through our [community portal]
(https://community.eyefi.com/eyefi/categories/eyefi_developer_api).

# Authentication

Eyefi's Cloud API uses the [OAuth 2.0 authorization framework](http://tools.ietf.org/html/rfc6749) 
for simple-but-effective authentication and authorization.

All requests must happen over **https**.

## Obtaining an Authentication Token

An end user will obtain an authentication token from the [Eyefi Web App](https://app.eyefi.com).
Under the account menu tree there is an option called "Developer".  This controls the current list
of authentication tokens.  Select the '+' icon to generate a new authentication token to be used
to contact the API.  If you wish to remove or regenerate authentication tokens this can also be done
from this screen.

## Using the Authentication Token
 
Once the token has been obtained, it should be passed with every API call in an authorization header:

```
Authorization: Bearer ACCESS_TOKEN
```

For example if you were using curl to get the list of albums in a user's account, it would look like this:

```
curl https://api.eyefi.com/3/albums
    -H 'Authorization: Bearer ACCESS_TOKEN'
    -X 'GET'
```

# API General Use

## Requests

Each of the API endpoints has a series of operations with a mixture of POST, GET, PUT, and DELETE.

For POST and PUT requests, the data can be passed in the body using content 
type `application/x-www-form-urlencoded`:

```
curl https://api.eyefi.com/3/albums
    -H 'Authorization: Bearer ACCESS_TOKEN' 
    -X 'POST' 
    -d 'name=NAME' 
```

or content type `application/json`:

```
curl https://api.eyefi.com/3/albums
    -H 'Authorization: Bearer ACCESS_TOKEN' 
    -X 'POST'
    -H 'Content-Type: application/json' 
    -d '{"name":"NAME"}'
```

### Note on documentation

For each API call there are a list of parameters that are required.  The first
parameters in the list, especially those that refer to the object id or the referenced object id, may be required 
in the URL and additional parameters are in the body.  An example is updating an album (rename album 12345678 to 
be "NEWNAME").  The documentation for Updating an Album will refer to the API call as:

```
PUT /albums/{albumId}
```

Which indicates that the {albumId} needs to be in the URL.  The parameters table looks like this:

<br>

| Name | Type | Description |
|------|:----:|-------------|
| albumId | integer | The ID of the album to update. |
| name | string | The new album name. |
| privacy | integer | Privacy setting for the album. Use 0 for private and 1 for public. Setting privacy to 1 also returns a share URL. |

Indicating the meaning of all parameters, some of which are in the URL and some of which should be form or JSON encoded
in the body.

A curl example then looks like this, with the object id in the URL "{albumId}" and the "name" parameter in the body:

```
curl https://api.eyefi.com/3/albums/12345678
    -H 'Authorization: Bearer ACCESS_TOKEN' 
    -X 'PUT'
    -H 'Content-Type: application/json' 
    -d '{"name":"NEWNAME"}'
```


## Responses

All responses come in JSON format in a simple envelope around a dictionary:

```JSON
{
    "id": 100000000,
    "name": "NAME",
    "file_count": FILE_COUNT    
}
```

or a list:

```JSON
[
    {
        "id": 100000001,
        "name": "NAME",
        "file_count": FILE_COUNT
    },
    {
        "id": 100000002,
        "name": "NAME",
        "file_count": FILE_COUNT
    }
]
```

## Status Codes

| Code | Description |
|--------|-------------|
| 200 | OK. |
| 201 | Resource created. Common for successful POSTs. |
| 204 | No content. Common for successful DELETEs when no data is returned. |
| 400 | Bad request. Common with malformed input such as invalid email address, bad JSON, etc. |
| 401 | Unauthorized. Invalid or expired access token. |
| 403 | Forbidden. Happens when trying to access a resource for which a user does not have permission. |
| 404 | Not found. |
| 409 | Conflict. Resource already exists, such as email already in use. |
| 500 | Internal server error. |

## Errors

When an error occurs the server returns a 4xx or 5xx status code and JSON error message that should be used purely for debugging:

```JSON
{
    "message": "Invalid email address"
}
```

## Miscellaneous Items

### Dates

All date fields are returned as [ISO 8601](https://www.google.com/search?q=%22ISO+8601%22)-formatted strings and are normalized to UTC.

```
2014-02-03T12:37:08+00:00
```

## Endpoint Listing

[Albums](endpoints/albums.md)
[Events](endpoints/events.md)
[Files](endpoints/files.md)
[Tags](endpoints/tags.md)
[Search](endpoints/search.md)
[Trash](endpoints/trash.md)






