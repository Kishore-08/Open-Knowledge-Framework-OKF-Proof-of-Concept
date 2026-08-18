---
id: fastapi-check-it-https-fastapi-tiangolo-com-tutorial-security-oauth2-657ba832
type: concept
title: Check it[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#check-it
  "Permanent link")
description: 'Run the server and go to the docs: <http://127.0.0.1:8000/docs>.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Check it[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#check-it "Permanent link")

Run the server and go to the docs: <http://127.0.0.1:8000/docs>.

You'll see the user interface like:

Authorize the application the same way as before.

Using the credentials:

Username: `johndoe`
Password: `secret`

Tip

Notice that nowhere in the code is the plaintext password "`secret`", we only have the hashed version.

Call the endpoint `/users/me/`, you will get the response as:

```
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "full_name": "John Doe",
  "disabled": false
}
```

If you open the developer tools, you could see how the data sent only includes the token, the password is only sent in the first request to authenticate the user and get that access token, but not afterwards:

Note

Notice the header `Authorization`, with a value that starts with `Bearer`.