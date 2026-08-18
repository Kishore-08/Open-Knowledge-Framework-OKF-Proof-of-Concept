---
id: fastapi-openapi-support-https-fastapi-tiangolo-com-tutorial-path-par-ec79efde
type: concept
title: OpenAPI support[¶](https://fastapi.tiangolo.com/tutorial/path-params/#openapi-support
  "Permanent link")
description: OpenAPI doesn't support a way to declare a *path parameter* to contain
  a *path* inside, as that could lead to scenarios that are difficult to test and
  define.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### OpenAPI support[¶](https://fastapi.tiangolo.com/tutorial/path-params/#openapi-support "Permanent link")

OpenAPI doesn't support a way to declare a *path parameter* to contain a *path* inside, as that could lead to scenarios that are difficult to test and define.

Nevertheless, you can still do it in **FastAPI**, using one of the internal tools from Starlette.

And the docs would still work, although not adding any documentation telling that the parameter should contain a path.