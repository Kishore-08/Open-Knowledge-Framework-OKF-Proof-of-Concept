---
id: fastapi-use-it-with-apirouter-https-fastapi-tiangolo-com-tutorial-fr-3854a0fd
type: concept
title: Use it with `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/frontend/#use-it-with-apirouter
  "Permanent link")
description: 'You can also add frontend files to an `APIRouter` and include it with
  a prefix:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/frontend/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Use it with `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/frontend/#use-it-with-apirouter "Permanent link")

You can also add frontend files to an `APIRouter` and include it with a prefix:

Python 3.10+

```
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

router.frontend("/", directory="dist", fallback="index.html")
app.include_router(router, prefix="/app")
```

In this example, frontend paths are served under `/app`.

Any regular *path operations* in the app will still take precedence, including in other routers.