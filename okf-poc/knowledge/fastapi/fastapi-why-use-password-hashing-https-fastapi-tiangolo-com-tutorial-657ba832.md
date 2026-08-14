---
id: fastapi-why-use-password-hashing-https-fastapi-tiangolo-com-tutorial-657ba832
type: concept
title: Why use password hashing[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#why-use-password-hashing
  "Permanent link")
description: If your database is stolen, the thief won't have your users' plaintext
  passwords, only the hashes.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Why use password hashing[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#why-use-password-hashing "Permanent link")

If your database is stolen, the thief won't have your users' plaintext passwords, only the hashes.

So, the thief won't be able to try to use that password in another system (as many users use the same password everywhere, this would be dangerous).