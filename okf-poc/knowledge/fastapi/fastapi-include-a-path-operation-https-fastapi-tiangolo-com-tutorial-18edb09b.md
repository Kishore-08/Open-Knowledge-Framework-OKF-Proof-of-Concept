---
id: fastapi-include-a-path-operation-https-fastapi-tiangolo-com-tutorial-18edb09b
type: concept
title: Include a *path operation*[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-a-path-operation
  "Permanent link")
description: We can also add *path operations* directly to the `FastAPI` app.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Include a *path operation*[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-a-path-operation "Permanent link")

We can also add *path operations* directly to the `FastAPI` app.

Here we do it... just to show that we can 🤷:

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

and it will work correctly, together with all the other *path operations* added with `app.include_router()`.

Very Technical Details

**Note**: this is a very technical detail that you probably can **just skip**.

---

The `APIRouter`s are not "mounted", they are not isolated from the rest of the application.

This is because we want to include their *path operations* in the OpenAPI schema and the user interfaces.

FastAPI keeps the original routers and path operations active, and combines the router prefixes, dependencies, tags, responses, and other metadata when handling requests and generating OpenAPI.