---
id: fastapi-custom-404-page-https-fastapi-tiangolo-com-tutorial-frontend-3854a0fd
type: concept
title: Custom 404 Page[¶](https://fastapi.tiangolo.com/tutorial/frontend/#custom-404-page
  "Permanent link")
description: 'You can also serve a static `404.html` page for missing frontend paths:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/frontend/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Custom 404 Page[¶](https://fastapi.tiangolo.com/tutorial/frontend/#custom-404-page "Permanent link")

You can also serve a static `404.html` page for missing frontend paths:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

app.frontend("/", directory="dist", fallback="404.html")
```

That response keeps a status code of `404`.

In this case, **FastAPI** won't serve `index.html` for missing frontend paths. It will return the `404.html` file instead.

Tip

By default, `fallback` has a value of `fallback="auto"`. With this, if a `404.html` file is found, it will be used as the fallback automatically.

So, you can normally omit the `fallback` argument.

This is useful with frontend tools that generate static HTML files for each page, like Astro.