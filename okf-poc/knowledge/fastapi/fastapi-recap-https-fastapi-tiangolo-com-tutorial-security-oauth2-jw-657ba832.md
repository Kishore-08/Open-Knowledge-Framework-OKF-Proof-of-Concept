---
id: fastapi-recap-https-fastapi-tiangolo-com-tutorial-security-oauth2-jw-657ba832
type: concept
title: Recap[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#recap "Permanent
  link")
description: With what you have seen up to now, you can set up a secure **FastAPI**
  application using standards like OAuth2 and JWT.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Recap[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#recap "Permanent link")

With what you have seen up to now, you can set up a secure **FastAPI** application using standards like OAuth2 and JWT.

In almost any framework handling the security becomes a rather complex subject quite quickly.

Many packages that simplify it a lot have to make many compromises with the data model, database, and available features. And some of these packages that simplify things too much actually have security flaws underneath.

---

**FastAPI** doesn't make any compromise with any database, data model or tool.

It gives you all the flexibility to choose the ones that fit your project the best.

And you can use directly many well maintained and widely used packages like `pwdlib` and `PyJWT`, because **FastAPI** doesn't require any complex mechanisms to integrate external packages.

But it provides you the tools to simplify the process as much as possible without compromising flexibility, robustness, or security.

And you can use and implement secure, standard protocols, like OAuth2 in a relatively simple way.

You can learn more in the **Advanced User Guide** about how to use OAuth2 "scopes", for a more fine-grained permission system, following these same standards. OAuth2 with scopes is the mechanism used by many big authentication providers, like Facebook, Google, GitHub, Microsoft, X (Twitter), etc. to authorize third party applications to interact with their APIs on behalf of their users.