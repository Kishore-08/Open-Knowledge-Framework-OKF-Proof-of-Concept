---
id: fastapi-import-the-apirouter-https-fastapi-tiangolo-com-tutorial-big-18edb09b
type: concept
title: Import the `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-apirouter
  "Permanent link")
description: 'Now we import the other submodules that have `APIRouter`s:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Import the `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-apirouter "Permanent link")

Now we import the other submodules that have `APIRouter`s:

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

As the files `app/routers/users.py` and `app/routers/items.py` are submodules that are part of the same Python package `app`, we can use a single dot `.` to import them using "relative imports".