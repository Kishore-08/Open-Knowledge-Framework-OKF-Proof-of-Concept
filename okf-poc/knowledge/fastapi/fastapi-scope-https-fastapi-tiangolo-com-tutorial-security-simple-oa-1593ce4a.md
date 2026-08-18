---
id: fastapi-scope-https-fastapi-tiangolo-com-tutorial-security-simple-oa-1593ce4a
type: concept
title: '`scope`[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#scope
  "Permanent link")'
description: The spec also says that the client can send another form field "`scope`".
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### `scope`[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#scope "Permanent link")

The spec also says that the client can send another form field "`scope`".

The form field name is `scope` (in singular), but it is actually a long string with "scopes" separated by spaces.

Each "scope" is just a string (without spaces).

They are normally used to declare specific security permissions, for example:

- `users:read` or `users:write` are common examples.
- `instagram_basic` is used by Facebook / Instagram.
- `https://www.googleapis.com/auth/drive` is used by Google.

Note

In OAuth2 a "scope" is just a string that declares a specific permission required.

It doesn't matter if it has other characters like `:` or if it is a URL.

Those details are implementation specific.

For OAuth2 they are just strings.