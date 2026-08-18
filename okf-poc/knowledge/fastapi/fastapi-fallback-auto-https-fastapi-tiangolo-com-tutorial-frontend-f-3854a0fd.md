---
id: fastapi-fallback-auto-https-fastapi-tiangolo-com-tutorial-frontend-f-3854a0fd
type: concept
title: Fallback Auto[¶](https://fastapi.tiangolo.com/tutorial/frontend/#fallback-auto
  "Permanent link")
description: By default, `app.frontend()` uses `fallback="auto"`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/frontend/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Fallback Auto[¶](https://fastapi.tiangolo.com/tutorial/frontend/#fallback-auto "Permanent link")

By default, `app.frontend()` uses `fallback="auto"`.

If there is a `404.html` file in the frontend directory, missing frontend paths serve that file with status code `404`.

Otherwise, if there is an `index.html` file, missing browser navigation paths serve `index.html`, which is what many frontend apps with client-side routing expect.

So, in most cases you can use `app.frontend("/", directory="dist")` without specifying the `fallback` argument.

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

app.frontend("/", directory="dist")
```