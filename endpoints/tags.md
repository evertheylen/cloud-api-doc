# Tags

Tags can be assigned to files to further categorize them.  Many of the APIs to apply tags are located under the /files
endpoint.  If a tag is applied to a file and it does not exist, it is automatically created.  Other options are
available under the /tags endpoint.

| Method | Description |
|--------|-------------|
| [GET /tags](#get-tags) | Gets a user's tags. |
| [GET /tags/{tagId}](#get-tagstagid) | Gets a specific tag. |
| [PUT /tags/{tagId}](#put-tagstagid) | Updates a tag name. |
| [DELETE /tags/{tagId}](#delete-tagstagid) | Deletes a tag. |

## GET /tags

Gets a user's tags.

### Authorization

`User`

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

## GET /tags/{tagId}

Gets a specific tag.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| tagId | integer | The ID of the tag to get. |

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
| 200 | Request has succeeded. |
| 404 | Album not found. |

## PUT /tags/{tagId}

Updates a tag.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| tagId | integer | The ID of the tag to update. |
| name | string | The new tag name. |

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
| 200 | Request has succeeded. |
| 400 | Bad request. |
| 404 | Album not found. |

## DELETE /tags/{tagId}

Deletes a tag.

### Authorization

`User`

### Parameters

| Name | Type | Description |
|------|:----:|-------------|
| tagId | integer | The ID of the tag to delete. |

### Status Codes

| Code | Reason |
|------|-------------|
| 404 | Album not found. |

