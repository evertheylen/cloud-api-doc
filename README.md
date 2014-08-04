# Overview

The Eyefi Cloud API is a RESTful API that uses OAuth 2.0 for authentication.

**NOTE:** Access to the API is currently limited and granted on a case by case basis. For access please [apply](https://docs.google.com/forms/d/1kxAlAWullYE-gOHMa3-5ujmccB-xKx1HewlPBGz9Ev0/viewform). We look forward to hearing from you.

## Important Terms

* **Users:** Users are user accounts.
* **Events:** Events are the default file organization structure in the Eyefi Cloud API. Events are groups of photos organized by date (i.e., the date on which the pictures were created, or a range of dates covering a vacation or holiday). Photos in an event are organized chronologically from oldest to newest. Files will always exist in a single event.

# Authentication

Eyefi's Cloud API uses the [OAuth 2.0 authorization framework](http://tools.ietf.org/html/rfc6749) 
for simple-but-effective authentication and authorization.

All requests must happen over **https**.

## Authorization Code Grant Flow

Redirect the user to our authorization URL:

```
https://api.eyefi.com/oauth/authorize?client_id=CLIENT_ID&response_type=code&redirect_uri=REDIRECT_URI&state=STATE
```

**Note:** The **state** parameter is optional but recommended. Read more about it [here](http://tools.ietf.org/html/rfc6749#section-4.1.1).

Once the user successfully authenticates and authorizes your application, we will redirect them to your redirect URI with a **code** parameter:

```
REDIRECT_URI?code=CODE&state=STATE
```

**Note:** The **code** is valid for up to 10 minutes and is invalidated on first use.

Next you will POST this **code** to the token endpoint to receive a **access_token** and **refresh_token**.

```
curl https://api.eyefi.com/oauth/token \
    -F 'client_id=CLIENT_ID' \
    -F 'client_secret=CLIENT_SECRET' \
    -F 'grant_type=authorization_code' \
    -F 'redirect_uri=REDIRECT_URI' \
    -F 'code=CODE'
```

**Note:** The **redirect_uri** must be the same one used in the authorization request.

If successful, this call returns an access token and a long-lived refresh 
token:

```JSON
200 OK
{
    "access_token": "JDJhJDA4JFhpbXBLVzM4MldOamFIUkcwUS9FRE9tZmJreVVSdlROVWdlY0VSbGpOcjlTcGlYRlRkNzZT",
    "expires_in": 86400,
    "refresh_token":"JDJ5JDA4JHd1dzFhQUdHc004czJ2dUtreVYzbU9oUkx0U0c4MDJhTjNnWjZMc1pwYTVuTXBzRUNuYklh",
    "token_type":"Bearer"
}
```

`expires_in` indicates the number of seconds that the access token may remain 
valid. The refresh token may remain valid for up to six months.

If unsuccessful, this call returns an error with a description. Examples:

```JSON
400 Bad Request
{
    "error": "invalid_request",
    "error_description": "Client ID or signature mismatch."
}
```

```JSON
401 Unauthorized
{
    "error": "invalid_request",
    "error_description": "Invalid authorization code."
}
```

# Endpoints

Eyefi's Cloud API is a RESTful API. Every endpoint may support up to four different 
HTTP verbs. GET requests return information about a resource, POST requests 
create resources, PUT requests update resources, and DELETE deletes resources.

* [Users](endpoints/users.md)
* [Events](endpoints/events.md)

## Requests

All requests must happen over **https** at the base URL 
**https://api.eyefi.com/3**. The access token is passed in the header for 
requests that require authorization.

Example GET request:

```
curl https://api.eyefi.com/3/users/me \
    -H 'Authorization: Bearer ACCESS_TOKEN'
```

For POST and PUT requests, the data can be passed in the body using content 
type `application/x-www-form-urlencoded`:

```
curl https://api.eyefi.com/3/users/me \
    -H 'Authorization: Bearer ACCESS_TOKEN' \
    -X 'PUT' \
    -d 'name=NAME' \
    -d 'email=EMAIL'
```

or content type `application/json`:

```
curl https://api.eyefi.com/3/users/me \
    -H 'Authorization: Bearer ACCESS_TOKEN' \
    -X 'PUT' \
    -H 'Content-Type: application/json' \
    -d '{"name":"NAME","email":"EMAIL"}'
```

## Responses

All responses come in JSON format in a simple envelope around a dictionary:

```JSON
{
    "id": 100000000,
    "name": "NAME",
    "email": "EMAIL"
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

### Status Codes

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

### Errors

When an error occurs the server returns a 4xx or 5xx status code and JSON error message that should be used purely for debugging:

```JSON
{
    "message": "Invalid email address"
}
```

### Dates

All date fields are returned as [ISO 8601](https://www.google.com/search?q=%22ISO+8601%22)-formatted strings and are normalized to UTC.

```
2014-02-03T12:37:08+00:00
```
