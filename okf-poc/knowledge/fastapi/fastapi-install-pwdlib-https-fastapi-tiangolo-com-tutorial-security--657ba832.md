---
id: fastapi-install-pwdlib-https-fastapi-tiangolo-com-tutorial-security--657ba832
type: concept
title: Install `pwdlib`[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pwdlib
  "Permanent link")
description: pwdlib is a great Python package to handle password hashes.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Install `pwdlib`[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pwdlib "Permanent link")

pwdlib is a great Python package to handle password hashes.

It supports many secure hashing algorithms and utilities to work with them.

The recommended algorithm is "Argon2".

Add `pwdlib` with Argon2 to your project:

```
$ uv add "pwdlib[argon2]"

---> 100%
```

Tip

With `pwdlib`, you could even configure it to be able to read passwords created by **Django**, a **Flask** security plug-in or many others.

So, you would be able to, for example, share the same data from a Django application in a database with a FastAPI application. Or gradually migrate a Django application using the same database.

And your users would be able to login from your Django app or from your **FastAPI** app, at the same time.