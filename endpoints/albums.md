# Albums

An album is a user-created collection of files. A file can be in any number of albums. Albums can be named and shared.

| Method | Description |
|--------|-------------|
| [POST /albums](#post-albums) | Adds a user album. |
| [GET /albums](#get-albums) | Gets a user's albums. |
| [GET /albums/{albumId}](#get-albumsalbumid) | Gets a specific album. |
| [PUT /albums/{albumId}](#put-albumsalbumid) | Updates an album. |
| [POST /albums/{albumId}/files](#post-albumsalbumidfiles) | Adds files to a user album. |
| [GET /albums/{albumId}/files](#get-albumsalbumidfiles) | Gets the files in an album. |
| [PUT /albums/{albumId}/files](#put-albumsalbumidfiles) | Updates album files. Files are listed as a comma-separated array. |
| [DELETE /albums/{albumId}/files/{fileId}](#delete-albumsalbumidfilesfileid) | Removes a file from an album. |
| [DELETE /albums/{albumId}](#delete-albumsalbumid) | Deletes an album. |

## POST /albums

Adds a user album.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| name | string | The album's name. |

### Returns

```JSON
{
    "id": "integer",
    "name": "string",
    "file_count": "integer",
    "start_date": "Date",
    "end_date": "Date",
    "privacy": "integer",
    "share_url": "string",
    "thumbnails": {
        "url": "string",
        "s640": "string",
        "s1280": "string",
        "s2048": "string"
    }
}
```

### Response

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | Album ID. |
| name | string | Album name. |
| file_count | integer | Number of files in the album. |
| start_date | Date | Date of the earliest photo in the album. |
| end_date | Date | Date of the latest photo in the album. |
| privacy | integer | Privacy setting for the album. Use 0 for private and 1 for public. Setting privacy to 1 also returns a share URL. |
| share_url | string | URL for sharing the album. |
| thumbnails / url | string | Base URL for the thumbnail; append file size to return specific sizes. |
| thumbnails / s640 | string | Returns a 640px thumbnail. |
| thumbnails / s1280 | string | Returns a 1280px thumbnail. |
| thumbnails / s2048 | string | Returns a 2048px thumbnail. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |

## GET /albums

Gets a user's albums.

### Authorization

`User`

### Response

```JSON
[
    {
        "id": "integer",
        "name": "string",
        "file_count": "integer",
        "start_date": "Date",
        "end_date": "Date",
        "privacy": "integer",
        "share_url": "string",
        "thumbnails": {
            "url": "string",
            "s640": "string",
            "s1280": "string",
            "s2048": "string"
        }
    }
]
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | Album ID. |
| name | string | Album name. |
| file_count | integer | Number of files in the album. |
| start_date | Date | Date of the earliest photo in the album. |
| end_date | Date | Date of the latest photo in the album. |
| privacy | integer | Privacy setting for the album. Use 0 for private and 1 for public. Setting privacy to 1 also returns a share URL. |
| share_url | string | URL for sharing the album. |
| thumbnails / url | string | Base URL for the thumbnail; append file size to return specific sizes. |
| thumbnails / s640 | string | Returns a 640px thumbnail. |
| thumbnails / s1280 | string | Returns a 1280px thumbnail. |
| thumbnails / s2048 | string | Returns a 2048px thumbnail. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 404 | Album not found. |

## GET /albums/{albumId}

Gets a specific album.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| albumId | integer | The ID of the album to get. |

### Returns

```JSON
{
    "id": "integer",
    "name": "string",
    "file_count": "integer",
    "start_date": "Date",
    "end_date": "Date",
    "privacy": "integer",
    "share_url": "string",
    "thumbnails": {
        "url": "string",
        "s640": "string",
        "s1280": "string",
        "s2048": "string"
    }
}
```

### Response

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | Album ID. |
| name | string | Album name. |
| file_count | integer | Number of files in the album. |
| start_date | Date | Date of the earliest photo in the album. |
| end_date | Date | Date of the latest photo in the album. |
| privacy | integer | Privacy setting for the album. Use 0 for private and 1 for public. Setting privacy to 1 also returns a share URL. |
| share_url | string | URL for sharing the album. |
| thumbnails / url | string | Base URL for the thumbnail; append file size to return specific sizes. |
| thumbnails / s640 | string | Returns a 640px thumbnail. |
| thumbnails / s1280 | string | Returns a 1280px thumbnail. |
| thumbnails / s2048 | string | Returns a 2048px thumbnail. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 404 | Album not found. |

## PUT /albums/{albumId}

Updates an album.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| albumId | integer | The ID of the album to update. |
| name | string | The new album name. |
| privacy | integer | Privacy setting for the album. Use 0 for private and 1 for public. Setting privacy to 1 also returns a share URL. |

### Returns

```JSON
{
    "id": "integer",
    "name": "string",
    "file_count": "integer",
    "start_date": "Date",
    "end_date": "Date",
    "privacy": "integer",
    "share_url": "string",
    "thumbnails": {
        "url": "string",
        "s640": "string",
        "s1280": "string",
        "s2048": "string"
    }
}
```

### Response

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | Album ID. |
| name | string | Album name. |
| file_count | integer | Number of files in the album. |
| start_date | Date | Date of the earliest photo in the album. |
| end_date | Date | Date of the latest photo in the album. |
| privacy | integer | Privacy setting for the album. Use 0 for private and 1 for public. Setting privacy to 1 also returns a share URL. |
| share_url | string | URL for sharing the album. |
| thumbnails / url | string | Base URL for the thumbnail; append file size to return specific sizes. |
| thumbnails / s640 | string | Returns a 640px thumbnail. |
| thumbnails / s1280 | string | Returns a 1280px thumbnail. |
| thumbnails / s2048 | string | Returns a 2048px thumbnail. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 400 | Bad request. |
| 404 | Album not found. |

## GET /albums/{albumId}/files

Gets the files in an album.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| albumId | integer | ID of the album from which to get files. |

### Returns

```JSON
[
    {
        "id": "integer",
        "name": "string",
        "date_time_taken": "Date",
        "size": {
            "width": "integer",
            "height": "integer"
        },
        "thumbnails": {
            "url": "string",
            "s640": "string",
            "s1280": "string",
            "s2048": "string"
        }
    }
]
```

### Response

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | File ID. |
| name | string | File name. |
| date_time_taken | Date | Date and time the file was created. |
| size / width | integer | The file's width in pixels. |
| size / height | integer | The file's height in pixels. |
| thumbnails / url | string | Base URL for the thumbnail; append file size to return specific sizes. |
| thumbnails / s640 | string | Returns a 640px thumbnail. |
| thumbnails / s1280 | string | Returns a 1280px thumbnail. |
| thumbnails / s2048 | string | Returns a 2048px thumbnail. |

### Status Codes

| Code | Reason |
| 200 | Request has succeeded. |
| 404 | Album not found. |

## PUT /albums/{albumId}/files

Updates album files. Files are listed as a comma-separated array. Can be used to re-order the files in an album.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| fileId | integer | ID of the file to add to the album. |

### Returns

Returns a list of the updated files.

### Response

```JSON
[
    {
        "id": "integer",
        "name": "string",
        "date_time_taken": "Date",
        "size": {
            "width": "integer",
            "height": "integer"
        },
        "thumbnails": {
            "url": "string",
            "s640": "string",
            "s1280": "string",
            "s2048": "string"
        }
    }
]
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | File ID. |
| name | string | File name. |
| date_time_taken | Date | Date and time the file was created. |
| size / width | integer | The file's width in pixels. |
| size / height | integer | The file's height in pixels. |
| thumbnails / url | string | Base URL for the thumbnail; append file size to return specific sizes. |
| thumbnails / s640 | string | Returns a 640px thumbnail. |
| thumbnails / s1280 | string | Returns a 1280px thumbnail. |
| thumbnails / s2048 | string | Returns a 2048px thumbnail. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 404 | Album not found. |

## DELETE /albums/{albumId}/files/{fileId}

Removes a file from an album.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| albumId | integer | ID of the album to modify. |
| fileId | integer | ID of the file to remove from the album. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 404 | Album not found. |

## DELETE /albums/{albumId}

Deletes an album. This is not recoverable. Does not affect the files contained in the album.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| albumId | integer | The ID of the album to delete. |

### Status Codes

| Code | Reason |
|------|-------------|
| 404 | Album not found. |