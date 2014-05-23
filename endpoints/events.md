# Events

Events are groups of photos organized by date (i.e., the date on which the pictures were 
created, or a range of dates covering a vacation or holiday).

| Method | Description |
|--------|-------------|
| [GET /events](#get-events) | Gets a user's events. |
| [GET /events/{eventId}](#get-eventseventid) | Returns an array of the user's events. |
| [GET /events/{eventId}/files](#get-eventseventidfiles) | Returns an array of files. |

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
    "id": 12160345,
    "name": "Event Name",
    "file_count": 6,
    "start_date": "2014-03-22T12:30:26+00:00",
    "end_date": "2014-03-22T13:47:50+00:00"
  }
]
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | The event's ID. |
| name | string | The event's name. |
| file_count | integer | The number of files in the event. |
| start_date | date-time | The event's start date. |
| end_date | date-time | The event's end date. |

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

### Returns

An event.

### Response

```JSON
{
  "id": 12160345,
  "name": "Event Name",
  "file_count": 6,
  "start_date": "2014-03-22T12:30:26+00:00",
  "end_date": "2014-03-22T13:47:50+00:00"
}
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | The event's ID. |
| name | string | The event's name. |
| file_count | integer | The number of files in the event. |
| start_date | date-time | The event's start date. |
| end_date | date-time | The event's end date. |

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

### Returns

Returns an array of files.

### Response

```JSON
[
  {
    "id": 2605844341,
    "name": "IMG_1138.JPG",
    "date_time_taken": "2014-03-07T09:05:29+00:00",
    "size": {
      "width": 1540,
      "height": 2048
    },
    "bytes": 890278,
    "exif": {
      "camera": "Canon EOS 60D",
      "aperture": "8.0",
      "shutter_speed": "1/250",
      "iso": "250",
      "focal_length": "55.0 mm",
      "flash": "Off, Did not fire"
    },
    "gps": {
      "lat": null,
      "lng": null
    },
    "media": "https://api.eyefi.com/3/files/2605844341/media?signature=d7be17dd695l8f0d7cc613fb52e6b1e093b4fb22",
    "thumbnails": {
      "s320": "https://api.eyefi.com/3/files/2605844341/thumbnails/a7be17dd695l8f0d7cc613fb52e6b1e093b4fb22/s320/image.jpg",
      "s640": "https://api.eyefi.com/3/files/2605844341/thumbnails/a7be17dd695l8f0d7cc613fb52e6b1e093b4fb22/s640/image.jpg",
      "s1280": "https://api.eyefi.com/3/files/2605844341/thumbnails/a7be17dd695l8f0d7cc613fb52e6b1e093b4fb22/s1280/image.jpg",
      "s2048": "https://api.eyefi.com/3/files/2605844341/thumbnails/a7be17dd695l8f0d7cc613fb52e6b1e093b4fb22/s2048/image.jpg"
    }
  }
]
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | File ID. |
| name | string | File name. |
| date_time_taken | date-time | Date and time the file was taken. |
| size / width | integer | The file's width in pixels. |
| size / height | integer | The file's height in pixels. |
| bytes | integer | The file's size in bytes. |
| exif / camera | string | Camera used to take the photo. |
| exif / aperture | string | Aperture used to take the photo. |
| exif / shutter_speed | string | Shutter speed used to take the photo. |
| exif / iso | string | ISO  used to take the photo. |
| exif / focal_length | string | Focal length used to take the photo. |
| exif / flash | string | Flash used to take the photo. |
| gps / lat | float | Latitude. |
| gps / lng | float | Longitude. |
| thumbnails / s320 | string | Returns a 320px thumbnail. |
| thumbnails / s640 | string | Returns a 640px thumbnail. |
| thumbnails / s1280 | string | Returns a 1280px thumbnail. |
| thumbnails / s2048 | string | Returns a 2048px thumbnail. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 404 | Event not found. |
