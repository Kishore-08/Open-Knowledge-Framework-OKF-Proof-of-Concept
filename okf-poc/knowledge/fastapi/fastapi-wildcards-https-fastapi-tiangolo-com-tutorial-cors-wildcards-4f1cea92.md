---
id: fastapi-wildcards-https-fastapi-tiangolo-com-tutorial-cors-wildcards-4f1cea92
type: concept
title: Wildcards[¶](https://fastapi.tiangolo.com/tutorial/cors/#wildcards "Permanent
  link")
description: It's also possible to declare the list as `"*"` (a "wildcard") to say
  that all are allowed.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cors/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Wildcards[¶](https://fastapi.tiangolo.com/tutorial/cors/#wildcards "Permanent link")

It's also possible to declare the list as `"*"` (a "wildcard") to say that all are allowed.

But that will only allow certain types of communication, excluding everything that involves credentials: Cookies, Authorization headers like those used with Bearer Tokens, etc.

So, for everything to work correctly, it's better to specify explicitly the allowed origins.