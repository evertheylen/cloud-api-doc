# Events

An event is a collection of photos. By default, events are created per day. The default name of an event is the full name of the date on which the photos were taken (e.g., January 20, 2015).

| Method | Description |
|--------|-------------|
| [GET /events](#get-events) | Gets a user's events. |
| [GET /events/{eventId}](#get-eventseventid) | Returns an array of the user's events. |
| [PUT /events/{eventId}](#put-eventseventid) | Updates a user event. |
| [GET /events/{eventId}/files](#get-eventseventidfiles) | Returns an array of the files in an event. |

## GET /events

Gets a user's events.

### Authorization

`User`

### Returns

Returns an array of the user's events.

### Response

```JSON
[
    {
        "id": "integer",
        "name": "string",
        "file_count": "integer",
        "start_date": "Date",
        "end_date": "Date"
    }
]
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | The event's ID. |
| name | string | The event's name. |
| file_count | integer | The number of files in the event. |
| start_date | Date | The event's start date. |
| end_date | Date | The event's end date. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |

## GET /events/{eventId}

Gets a user event.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| eventId | integer | The ID of the event to get. |

### Response

```JSON
[
    {
        "id": "integer",
        "name": "string",
        "file_count": "integer",
        "start_date": "Date",
        "end_date": "Date"
    }
]
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | The event's ID. |
| name | string | The event's name. |
| file_count | integer | The number of files in the event. |
| start_date | Date | The event's start date. |
| end_date | Date | The event's end date. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 404 | Event not found. |

## PUT /events/{eventId}

Updates an event.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| eventId | integer | ID of the event to update. |
| name | string | New event name. |
| start_date | Date | The new start date for the event. |
| end_date | Date | The new end date for the event. |

### Response

```JSON
{
    "id": "integer",
    "name": "string",
    "file_count": "integer",
    "start_date": "Date",
    "end_date": "Date"
}
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | The event's ID. |
| name | string | The event's name. |
| file_count | integer | The number of files in the event. |
| start_date | Date | The event's start date. |
| end_date | Date | The event's end date. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 404 | Event not found. |

## GET /events/{eventId}/files

Gets the files in an event.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| eventId | integer | The ID of the event for which to get files. |
| page | integer | The page number to retrieve when retrieving multiple pages of files. |
| per_page | integer | The number of files per page to retrieve when retrieving multiple pages of files (default is 100). |

### Returns

Returns an array of files.

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
| 404 | Event not found. |