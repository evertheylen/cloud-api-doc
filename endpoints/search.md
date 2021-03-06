# Search

| Method | Description |
|--------|-------------|
| [GET /search/files](#get-searchfiles) | Gets a list of files that match the search criteria. |

## GET /search/files

Creates an ad-hoc search and returns the file list.

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| page | integer | The page number to retrieve when retrieving multiple pages of files. |
| per_page | integer | The number of files per page to retrieve when retrieving multiple pages of files (default is 100). |
| favorite | boolean | Indicator if the file is favorited (not yet implemented in client UI). |
| in_trash | boolean | Indicator if trash is to be searched (default is false). |
| has_geodata | boolean | Indicator if geodata is required for the file to be included in the search results. |
| geo_lat | float | Geographic Latitude. Requres geo_lon and geo_distance. |
| geo_lon | float | Geographic Longitude. Requres geo_lat and geo_distance. |
| geo_distance | string | Geographic Distance. Integer format followed by "mi" or "km" for miles or kilometers. Requires geo_lat and geo_lon. If Geographic coordinates are specified in the search criteria, search results will include the file if it fits within the specified area. |
| album_ids | string | Files need to be in the list of album IDs to be included in search results. Formatted as a string with comma-separated integers. |
| event_ids | string | Files need to be in the list of event IDs to be included in search results. Formatted as a string with comma-separated integers. |
| tag_ids | string | Files need to be in the list of tag IDs to be included in search results. Formatted as a string with comma-separated integers. |
| camera | string | Camera name from exif data to include in search results. This is a keyword match as opposed to a full string match. |
| date_from | string | Start date in the format of YYYY-MM-DD. Photos need to be taken after date_from to be included in search results. |
| date_to | string | End Date in the format of YYYY-MM-DD. Photos need to be taken before date_to to be included in search results. |
| page | integer | Request page to allow for paged search results (default is 1). |
| per_page | integer | Items per page (default is 10). |

### Response

```JavaScript
{
    "total_count": "integer",
    "items": [
        {
            "id": "integer",
            "name": "string",
            "media": "string",
            "bytes": "integer",
            "date_time_taken": "date-time",
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
| date_time_taken | date-time | Date and time the file was created. |
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
| 200 | Request has succeeded. |
