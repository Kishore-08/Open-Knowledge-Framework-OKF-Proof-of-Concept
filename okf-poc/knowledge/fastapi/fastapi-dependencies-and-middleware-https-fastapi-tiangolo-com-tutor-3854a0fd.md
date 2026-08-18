---
id: fastapi-dependencies-and-middleware-https-fastapi-tiangolo-com-tutor-3854a0fd
type: concept
title: Dependencies and Middleware[¶](https://fastapi.tiangolo.com/tutorial/frontend/#dependencies-and-middleware
  "Permanent link")
description: Frontend responses run inside the normal **FastAPI** application, so
  HTTP middleware applies to them.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/frontend/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Dependencies and Middleware[¶](https://fastapi.tiangolo.com/tutorial/frontend/#dependencies-and-middleware "Permanent link")

Frontend responses run inside the normal **FastAPI** application, so HTTP middleware applies to them.

Dependencies from the app, from an `APIRouter`, and from `include_router()` also apply to frontend responses. This can be useful for protecting a frontend with cookie authentication or similar.

Dependencies can also modify response headers and add background tasks, as with normal *path operations*.