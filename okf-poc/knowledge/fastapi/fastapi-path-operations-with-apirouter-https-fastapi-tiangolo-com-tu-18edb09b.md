---
id: fastapi-path-operations-with-apirouter-https-fastapi-tiangolo-com-tu-18edb09b
type: concept
title: '*Path operations* with `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#path-operations-with-apirouter
  "Permanent link")'
description: And then you use it to declare your *path operations*.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### *Path operations* with `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#path-operations-with-apirouter "Permanent link")

And then you use it to declare your *path operations*.

Use it the same way you would use the `FastAPI` class:

Python 3.8+

app/routers/users.py

```
from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
```

You can think of `APIRouter` as a "mini `FastAPI`" class.

All the same options are supported.

All the same `parameters`, `responses`, `dependencies`, `tags`, etc.

Tip

In this example, the variable is called `router`, but you can name it however you want.

We are going to include this `APIRouter` in the main `FastAPI` app, but first, let's check the dependencies and another `APIRouter`.