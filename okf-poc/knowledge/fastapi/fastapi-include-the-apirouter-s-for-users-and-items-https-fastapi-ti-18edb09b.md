---
id: fastapi-include-the-apirouter-s-for-users-and-items-https-fastapi-ti-18edb09b
type: concept
title: Include the `APIRouter`s for `users` and `items`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-apirouters-for-users-and-items
  "Permanent link")
description: 'Now, let''s include the `router`s from the submodules `users` and `items`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Include the `APIRouter`s for `users` and `items`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-apirouters-for-users-and-items "Permanent link")

Now, let's include the `router`s from the submodules `users` and `items`:

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

Note

`users.router` contains the `APIRouter` inside of the file `app/routers/users.py`.

And `items.router` contains the `APIRouter` inside of the file `app/routers/items.py`.

With `app.include_router()` we can add each `APIRouter` to the main `FastAPI` application.

It will include all the routes from that router as part of it.

Technical Details

FastAPI keeps the original `APIRouter` and its `APIRoute`s active when the router is included in the main application.

That means custom `APIRouter` and `APIRoute` subclasses can still participate after the router is included.

Tip

You don't have to worry about performance when including routers.

This is designed to be lightweight and to avoid adding overhead to each request.

So it won't affect performance. ⚡