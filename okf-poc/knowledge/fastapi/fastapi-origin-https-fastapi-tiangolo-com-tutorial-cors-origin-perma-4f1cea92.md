---
id: fastapi-origin-https-fastapi-tiangolo-com-tutorial-cors-origin-perma-4f1cea92
type: concept
title: Origin[¶](https://fastapi.tiangolo.com/tutorial/cors/#origin "Permanent link")
description: An origin is the combination of protocol (`http`, `https`), domain (`myapp.com`,
  `localhost`, `localhost.tiangolo.com`), and port (`80`, `443`, `8080`).
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cors/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Origin[¶](https://fastapi.tiangolo.com/tutorial/cors/#origin "Permanent link")

An origin is the combination of protocol (`http`, `https`), domain (`myapp.com`, `localhost`, `localhost.tiangolo.com`), and port (`80`, `443`, `8080`).

So, all these are different origins:

- `http://localhost`
- `https://localhost`
- `http://localhost:8080`

Even if they are all in `localhost`, they use different protocols or ports, so, they are different "origins".