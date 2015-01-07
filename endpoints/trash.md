# Trash

| Method | Description |
|--------|-------------|
| [GET /trash/files](#get-trashfiles) | Gets the files in the user's trash. |
| [DELETE /trash/files](#delete-trashfiles) | Empties the trash. |
| [POST /trash/files/{fileId}/restore](#post-trashfilesfileidrestore) | Restore a file from trash. |

## GET /trash/files

Gets the files in the user's trash.

### Authorization

`User`

### Returns

Returns an array of the the files in the user's trash.

### Response

```javascript
{
  "id": "integer",
  "name": "string",
  "date_time_taken": "Date",
  "size": {
    "width": "integer",
    "height": "integer"
  },
  "thumbnails": {
    "url": "string"
    "s640": "string",
    "s1280": "string",
    "s2048": "string",
  }
}
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | File ID. |
| name | string | File name. |
| date_time_taken | Date | Date and time the file was taken. |
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
| 401 | Not authorized. |

## DELETE /trash/files

Empties the trash.

### Authorization

`User`

### Status Codes

| Code | Reason |
|------|--------|
| 204 | No content. |

## POST /trash/files/{fileId}/restore

Restores a file from the trash.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| fileId | integer | The ID of the file to restore. |

### Status Codes

| Code | Reason |
|------|-------------|
| 204 | No content. |
| 404 | File not found. |
