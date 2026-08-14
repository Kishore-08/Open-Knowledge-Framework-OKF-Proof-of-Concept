---
id: fastapi-include-an-apirouter-in-another-https-fastapi-tiangolo-com-t-18edb09b
type: concept
title: Include an `APIRouter` in another[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-in-another
  "Permanent link")
description: 'The same way you can include an `APIRouter` in a `FastAPI` application,
  you can include an `APIRouter` in another `APIRouter` using:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Include an `APIRouter` in another[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-in-another "Permanent link")

The same way you can include an `APIRouter` in a `FastAPI` application, you can include an `APIRouter` in another `APIRouter` using:

```
router.include_router(other_router)
```

You can do this before or after including `router` in the `FastAPI` app. FastAPI will still include the *path operations* from `other_router` in routing and OpenAPI.

The same applies to *path operations* added later to the routers. They will be visible through the earlier inclusion too.

Technical Details

Avoid directly mutating `router.routes` after including a router. FastAPI treats router inclusion as live, so the original router and its routes remain part of routing and OpenAPI generation.

Use documented APIs such as path operation decorators and `.include_router()` to add routes and routers.

Treat `router.routes` as a lower-level route tree that can contain route definitions and included routers, and avoid relying on it as a flat list of final path operations.