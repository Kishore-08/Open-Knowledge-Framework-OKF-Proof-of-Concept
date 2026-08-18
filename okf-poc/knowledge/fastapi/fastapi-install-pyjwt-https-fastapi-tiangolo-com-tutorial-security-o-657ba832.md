---
id: fastapi-install-pyjwt-https-fastapi-tiangolo-com-tutorial-security-o-657ba832
type: concept
title: Install `PyJWT`[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pyjwt
  "Permanent link")
description: We need to install `PyJWT` to generate and verify the JWT tokens in Python.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Install `PyJWT`[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pyjwt "Permanent link")

We need to install `PyJWT` to generate and verify the JWT tokens in Python.

Add `pyjwt` to your project:

```
$ uv add pyjwt

---> 100%
```

Note

If you are planning to use digital signature algorithms like RSA or ECDSA, you should install the cryptography library dependency `pyjwt[crypto]`.

You can read more about it in the [PyJWT Installation docs](https://pyjwt.readthedocs.io/en/latest/installation.html).