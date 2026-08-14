---
id: fastapi-what-it-does-https-fastapi-tiangolo-com-tutorial-security-fi-3368d50f
type: concept
title: What it does[¶](https://fastapi.tiangolo.com/tutorial/security/first-steps/#what-it-does
  "Permanent link")
description: It will go and look in the request for that `Authorization` header, check
  if the value is `Bearer` plus some token, and will return the token as a `str`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/first-steps/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## What it does[¶](https://fastapi.tiangolo.com/tutorial/security/first-steps/#what-it-does "Permanent link")

It will go and look in the request for that `Authorization` header, check if the value is `Bearer` plus some token, and will return the token as a `str`.

If it doesn't see an `Authorization` header, or the value doesn't have a `Bearer` token, it will respond with a 401 status code error (`UNAUTHORIZED`) directly.

You don't even have to check if the token exists to return an error. You can be sure that if your function is executed, it will have a `str` in that token.

You can try it already in the interactive docs:

We are not verifying the validity of the token yet, but that's a start already.

## Recap[¶](https://fastapi.tiangolo.com/tutorial/security/first-steps/#recap "Permanent link")

So, in just 3 or 4 extra lines, you already have some primitive form of security.