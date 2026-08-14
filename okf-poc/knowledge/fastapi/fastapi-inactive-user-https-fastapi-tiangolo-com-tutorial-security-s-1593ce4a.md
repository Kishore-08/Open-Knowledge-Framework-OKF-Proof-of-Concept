---
id: fastapi-inactive-user-https-fastapi-tiangolo-com-tutorial-security-s-1593ce4a
type: concept
title: Inactive user[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#inactive-user
  "Permanent link")
description: 'Now try with an inactive user, authenticate with:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Inactive user[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#inactive-user "Permanent link")

Now try with an inactive user, authenticate with:

User: `alice`

Password: `secret2`

And try to use the operation `GET` with the path `/users/me`.

You will get an "Inactive user" error, like:

```
{
  "detail": "Inactive user"
}
```