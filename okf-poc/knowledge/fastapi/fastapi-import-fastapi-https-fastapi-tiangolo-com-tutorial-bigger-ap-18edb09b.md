---
id: fastapi-import-fastapi-https-fastapi-tiangolo-com-tutorial-bigger-ap-18edb09b
type: concept
title: Import `FastAPI`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi
  "Permanent link")
description: You import and create a `FastAPI` class as normally.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Import `FastAPI`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi "Permanent link")

You import and create a `FastAPI` class as normally.

And we can even declare [global dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/) that will be combined with the dependencies for each `APIRouter`:

Python 3.10+

app/main.py

```
from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
```