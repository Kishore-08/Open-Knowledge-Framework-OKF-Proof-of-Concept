---
id: fastapi-technical-details-https-fastapi-tiangolo-com-tutorial-backgr-3e17b7a1
type: concept
title: Technical Details[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#technical-details
  "Permanent link")
description: The class `BackgroundTasks` comes directly from [`starlette.background`](https://starlette.dev/background/).
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/background-tasks/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Technical Details[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#technical-details "Permanent link")

The class `BackgroundTasks` comes directly from [`starlette.background`](https://starlette.dev/background/).

It is imported/included directly into FastAPI so that you can import it from `fastapi` and avoid accidentally importing the alternative `BackgroundTask` (without the `s` at the end) from `starlette.background`.

By only using `BackgroundTasks` (and not `BackgroundTask`), it's then possible to use it as a *path operation function* parameter and have **FastAPI** handle the rest for you, just like when using the `Request` object directly.

It's still possible to use `BackgroundTask` alone in FastAPI, but you have to create the object in your code and return a Starlette `Response` including it.

You can see more details in [Starlette's official docs for Background Tasks](https://starlette.dev/background/).