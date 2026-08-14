---
id: fastapi-get-the-username-and-password-https-fastapi-tiangolo-com-tut-1593ce4a
type: concept
title: Get the `username` and `password`[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-the-username-and-password
  "Permanent link")
description: We are going to use **FastAPI** security utilities to get the `username`
  and `password`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Get the `username` and `password`[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-the-username-and-password "Permanent link")

We are going to use **FastAPI** security utilities to get the `username` and `password`.

OAuth2 specifies that when using the "password flow" (that we are using) the client/user must send `username` and `password` fields as form data.

And the spec says that the fields have to be named like that. So `user-name` or `email` wouldn't work.

But don't worry, you can show it as you wish to your final users in the frontend.

And your database models can use any other names you want.

But for the login *path operation*, we need to use these names to be compatible with the spec (and be able to, for example, use the integrated API documentation system).

The spec also states that the `username` and `password` must be sent as form data (so, no JSON here).