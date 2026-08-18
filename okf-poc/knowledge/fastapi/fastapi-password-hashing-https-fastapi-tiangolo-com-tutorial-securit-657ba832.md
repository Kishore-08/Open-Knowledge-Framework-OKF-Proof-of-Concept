---
id: fastapi-password-hashing-https-fastapi-tiangolo-com-tutorial-securit-657ba832
type: concept
title: Password hashing[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#password-hashing
  "Permanent link")
description: '"Hashing" means converting some content (a password in this case) into
  a sequence of bytes (just a string) that looks like gibberish.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Password hashing[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#password-hashing "Permanent link")

"Hashing" means converting some content (a password in this case) into a sequence of bytes (just a string) that looks like gibberish.

Whenever you pass exactly the same content (exactly the same password) you get exactly the same gibberish.

But you cannot convert from the gibberish back to the password.