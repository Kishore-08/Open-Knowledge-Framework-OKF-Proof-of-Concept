---
id: fastapi-oauth-1-https-fastapi-tiangolo-com-tutorial-security-oauth-1-c2d779e5
type: concept
title: OAuth 1[¶](https://fastapi.tiangolo.com/tutorial/security/#oauth-1 "Permanent
  link")
description: There was an OAuth 1, which is very different from OAuth2, and more complex,
  as it included direct specifications on how to encrypt the communication.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### OAuth 1[¶](https://fastapi.tiangolo.com/tutorial/security/#oauth-1 "Permanent link")

There was an OAuth 1, which is very different from OAuth2, and more complex, as it included direct specifications on how to encrypt the communication.

It is not very popular or used nowadays.

OAuth2 doesn't specify how to encrypt the communication, it expects you to have your application served with HTTPS.

Tip

In the section about **deployment** you will see how to set up HTTPS for free, using Traefik and Let's Encrypt.