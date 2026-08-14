---
id: fastapi-get-your-own-user-data-https-fastapi-tiangolo-com-tutorial-s-1593ce4a
type: concept
title: Get your own user data[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-your-own-user-data
  "Permanent link")
description: Now use the operation `GET` with the path `/users/me`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Get your own user data[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-your-own-user-data "Permanent link")

Now use the operation `GET` with the path `/users/me`.

You will get your user's data, like:

```
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "full_name": "John Doe",
  "disabled": false,
  "hashed_password": "fakehashedsecret"
}
```

If you click the lock icon and logout, and then try the same operation again, you will get an HTTP 401 error of:

```
{
  "detail": "Not authenticated"
}
```