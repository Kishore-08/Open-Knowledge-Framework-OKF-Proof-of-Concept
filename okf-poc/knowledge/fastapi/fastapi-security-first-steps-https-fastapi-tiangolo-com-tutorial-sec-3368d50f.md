---
id: fastapi-security-first-steps-https-fastapi-tiangolo-com-tutorial-sec-3368d50f
type: concept
title: Security - First Steps[¶](https://fastapi.tiangolo.com/tutorial/security/first-s
description: Let's imagine that you have your **backend** API in some domain.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/first-steps/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Security - First Steps[¶](https://fastapi.tiangolo.com/tutorial/security/first-steps/#security-first-steps "Permanent link")

Let's imagine that you have your **backend** API in some domain.

And you have a **frontend** in another domain or in a different path of the same domain (or in a mobile application).

And you want to have a way for the frontend to authenticate with the backend, using a **username** and **password**.

We can use **OAuth2** to build that with **FastAPI**.

But let's save you the time of reading the full long specification just to find those little pieces of information you need.

Let's use the tools provided by **FastAPI** to handle security.