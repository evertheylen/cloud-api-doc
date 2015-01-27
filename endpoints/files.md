# Files

A file is an individual photo. When a file is uploaded Eyefi Cloud stores the file itself, a series of thumbnails, and metadata about the file. Downloading a file consists of performing a GET on the "media" parameter for a file returned by a number of API calls including `GET /files` and `GET /files/{fileId}`.

| Method | Description |
|--------|-------------|
| [POST /files](#post-files) | Uploads a file up to 100 MB. |
| [GET /files](#get-files) | Gets a list of a user's files. |
| [GET /files/{fileId}](#get-filesfileid) | Gets the details for a specific file. |
| [POST /files/{fileId}/tags](#post-filesfileidtags) | Adds a tag to a file. |
| [GET /files/{fileId}/tags](#get-filesfileidtags) | Gets a file's tags. |
| [DELETE /files/{fileId}/tags/{tagId}](#delete-filesfileidtagstagid) | Removes a tag from a file. |
| [DELETE /files/{fileId}](#delete-filesfileid) | Deletes a file. |

## POST /files

Uploads a file up to 100 MB.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| File | file | The file to upload. |

### Response

```JSON
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
|------|--------|
| 400 | Number of files posted != 1, or file is invalid. |

## GET /files

Gets a list of a user's files.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| page | integer | The page number to retrieve when retrieving multiple pages of files. |
| per_page | integer | The number of files per page to retrieve when retrieving multiple pages of files (default is 100). |

### Response

```JSON
{
    "total_count": "integer",
    "items": [
        {
            "id": "integer",
            "name": "string",
            "media": "string",
            "bytes": "integer",
            "date_time_taken": "Date",
            "size": {
                "width": "integer",
                "height": "integer"
            },
            "exif": {
                "exposure_comp": "string",
                "shutter_speed": "string",
                "flash": "string",
                "metering_mode": "string",
                "lens": "string",
                "camera": "string",
                "iso": "string",
                "focal_length": "string",
                "aperture": "string"
            },
            "gps": {
                "lat": "float",
                "lng": "float"
            },
            "thumbnails": {
                "url": "string",
                "s640": "string",
                "s1280": "string",
                "s2048": "string"
            }
        }
    ]
}
```

| Key | Type | Description |
|------|:----:|-------------|
| total_count | integer | Total number of items available regardless of Page_Size. The "items" set size is limited by the Page_Size. |
| id | integer | File ID. |
| name | string | File name. |
| media | string | Full URL that can be used to download the file. |
| bytes | integer | Size of the file in bytes. |
| date_time_taken | Date | Date and time the file was created. |
| size / width | integer | The file's width in pixels. |
| size / height | integer | The file's height in pixels. |
| exif | dictionary | The file's exif information as provided by the camera. |
| gps / lat | float | The latitude where the photo was taken or synchronized. |
| gps / lng | float | The longitude where the photo was taken or synchronized. |
| thumbnails / url | string | Base URL for the thumbnail; append file size to return specific sizes. |
| thumbnails / s640 | string | Returns a 640px thumbnail. |
| thumbnails / s1280 | string | Returns a 1280px thumbnail. |
| thumbnails / s2048 | string | Returns a 2048px thumbnail. |

### Status Codes

## GET /files/{fileId}

Gets detailed information on a file.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| fileId | integer | ID of the file to get details onß. |

### Response

```JSON
{
    "id": "integer",
    "name": "string",
    "media": "string",
    "bytes": "integer",
    "date_time_taken": "Date",
    "size": {
        "width": "integer",
        "height": "integer"
    },
    "exif": {
        "exposure_comp": "string",
        "shutter_speed": "string",
        "flash": "string",
        "metering_mode": "string",
        "lens": "string",
        "camera": "string",
        "iso": "string",
        "focal_length": "string",
        "aperture": "string"
    },
    "gps": {
        "lat": "float",
        "lng": "float"
    },
    "thumbnails": {
        "url": "string",
        "s640": "string",
        "s1280": "string",
        "s2048": "string"
    }
}
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | File ID. |
| name | string | File name. |
| media | string | Full URL that can be used to download the file. |
| bytes | integer | Size of the file in bytes. |
| date_time_taken | Date | Date and time the file was created. |
| size / width | integer | The file's width in pixels. |
| size / height | integer | The file's height in pixels. |
| exif | dictionary | The file's exif information as provided by the camera. |
| gps / lat | float | The latitude where the photo was taken or synchronized. |
| gps / lng | float | The longitude where the photo was taken or synchronized. |
| thumbnails / url | string | Base URL for the thumbnail; append file size to return specific sizes. |
| thumbnails / s640 | string | Returns a 640px thumbnail. |
| thumbnails / s1280 | string | Returns a 1280px thumbnail. |
| thumbnails / s2048 | string | Returns a 2048px thumbnail. |

### Status Codes

| Code | Reason |
|------|-------------|
| 401 | Not authorized. |
| 404 | Not found. |

## POST /files/{fileId}/tags

Add a tag to a file.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| fileId | integer | The ID of the file to which to add a tag. |
| id | string | The tag ID to add to the file (optional; either ID or name must be specified). |
| name | string | The tag name to add to the file (optional; either ID or name must be specified. If the name is specified and does not exist, it will be created). |

### Returns

```JSON
{
    "id": "integer",
    "name": "string",
    "file_count": "integer"
}
```

### Response

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | Tag ID. |
| name | string | Tag name. |
| file_count | integer | Number of files with the tag attached. |

### Status Codes

| Code | Reason |
|------|-------------|
| 201 | Request has succeeded. |
| 400 | Bad request. |
| 404 | Tag not found. |

## GET /files/{fileId}/tags

Get tags on a file.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| fileId | integer | The ID of the file to get tags for. |

### Response

```JSON
[
    {
        "id": "integer",
        "name": "string",
        "file_count": "integer"
    }
]
```

| Key | Type | Description |
|------|:----:|-------------|
| tagId | integer | Tag ID. |
| name | string | Tag name. |
| file_count | integer | Number of files with the tag attached. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 404 | Tag not found. |

## DELETE /files/{fileId}/tags/{tagId}

Removes a tag from a file.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| fileId | integer | ID of the file from which to remove a tag. |
| tagId | integer | ID of the tag to remove. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 404 | Tag not found. |

## DELETE /files/{fileId}

Deletes a file.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| fileId | integer | ID of the file to delete. |

### Status Codes

| Code | Reason |
|------|-------------|
| 401 | Not authorized. |
| 404 | Not found. |