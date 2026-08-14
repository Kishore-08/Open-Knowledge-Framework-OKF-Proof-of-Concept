---
id: fastapi-avoid-name-collisions-https-fastapi-tiangolo-com-tutorial-bi-18edb09b
type: concept
title: Avoid name collisions[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#avoid-name-collisions
  "Permanent link")
description: We are importing the submodule `items` directly, instead of importing
  just its variable `router`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Avoid name collisions[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#avoid-name-collisions "Permanent link")

We are importing the submodule `items` directly, instead of importing just its variable `router`.

This is because we also have another variable named `router` in the submodule `users`.

If we had imported one after the other, like:

```
from .routers.items import router
from .routers.users import router
```

the `router` from `users` would overwrite the one from `items` and we wouldn't be able to use them at the same time.

So, to be able to use both of them in the same file, we import the submodules directly:

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