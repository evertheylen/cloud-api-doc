# Users

Users are user accounts.

| Method | Description |
|--------|-------------|
| [GET /users/me](#get-usersme) | Gets a user's account. |

## GET /users/me

Gets a user's account.

### Example

```
curl https://api.eyefi.com/3/users/me \
    -H 'Authorization: Bearer ACCESS_TOKEN'
```

### Response

```JSON
{
  "id": 1000000000,
  "name": "Sample Name",
  "email": "sampleemail@eyefi.com",
  "plus_expiration_date": "2014-03-22T12:30:26+00:00"
}
```

| Key | Type | Description |
|------|:----:|-------------|
| id | integer | User ID. |
| name | string | User name. |
| email | string | User email. |
| plus_expiration_date | date-time | Date and time at which a user's Eyefi Cloud membership expires. |

### Status Codes

| Code | Reason |
|------|-------------|
| 200 | Request has succeeded. |
| 404 | User not found. |