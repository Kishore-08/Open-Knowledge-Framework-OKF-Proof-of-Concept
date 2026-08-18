---
id: fastapi-client-side-routing-https-fastapi-tiangolo-com-tutorial-fron-3854a0fd
type: concept
title: Client-Side Routing[¶](https://fastapi.tiangolo.com/tutorial/frontend/#client-side-routing
  "Permanent link")
description: Many frontend apps, including **single-page apps** (SPAs), use client-side
  routing. A path like `/dashboard/settings` might not be a real file but the framework
  would take care of handling it.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/frontend/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Client-Side Routing[¶](https://fastapi.tiangolo.com/tutorial/frontend/#client-side-routing "Permanent link")

Many frontend apps, including **single-page apps** (SPAs), use client-side routing. A path like `/dashboard/settings` might not be a real file but the framework would take care of handling it.

So, if accessing that URL directly (instead of navigating through the app), the backend should serve the frontend app from `index.html`, so that the frontend framework can then handle the client-side routing.

For that, use `fallback="index.html"`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

app.frontend("/", directory="dist", fallback="index.html")
```

**FastAPI** uses this fallback only for `GET` and `HEAD` requests that explicitly accept HTML with `Accept: text/html` or `Accept: application/xhtml+xml`, as browser navigation requests normally do. Missing files like JavaScript, CSS, and images still return `404`.

Requests with other methods, like `POST` or `PUT`, to paths that only match the frontend fallback also return `404`. Regular **FastAPI** *path operations* still have higher priority than frontend routes.

Tip

By default, `fallback` has a value of `fallback="auto"`. In most cases you won't need to specify `fallback`. Read below for details.

This is what you would want with many frontend apps that use client-side routing, for example, React with TanStack Router, Vue, Angular, SvelteKit, or Solid.