---
id: fastapi-order-matters-https-fastapi-tiangolo-com-tutorial-path-param-ec79efde
type: concept
title: Order matters[¶](https://fastapi.tiangolo.com/tutorial/path-params/#order-matters
  "Permanent link")
description: When creating *path operations*, you can find situations where you have
  a fixed path.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Order matters[¶](https://fastapi.tiangolo.com/tutorial/path-params/#order-matters "Permanent link")

When creating *path operations*, you can find situations where you have a fixed path.

Like `/users/me`, let's say that it's to get data about the current user.

And then you can also have a path `/users/{user_id}` to get data about a specific user by some user ID.

Because *path operations* are evaluated in order, you need to make sure that the path for `/users/me` is declared before the one for `/users/{user_id}`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

Otherwise, the path for `/users/{user_id}` would match also for `/users/me`, "thinking" that it's receiving a parameter `user_id` with a value of `"me"`.

Similarly, you cannot redefine a path operation:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]
```

The first one will always be used since the path matches first.