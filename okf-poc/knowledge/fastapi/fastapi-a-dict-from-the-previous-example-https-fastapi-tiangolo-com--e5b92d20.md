---
id: fastapi-a-dict-from-the-previous-example-https-fastapi-tiangolo-com--e5b92d20
type: concept
title: A `dict` from the previous example[¶](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#a-dict-from-the-previous-example
  "Permanent link")
description: 'In the previous example, we were returning a `dict` from our dependency
  ("dependable"):'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## A `dict` from the previous example[¶](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#a-dict-from-the-previous-example "Permanent link")

In the previous example, we were returning a `dict` from our dependency ("dependable"):

Python 3.10+

```
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
```

But then we get a `dict` in the parameter `commons` of the *path operation function*.

And we know that editors can't provide a lot of support (like completion) for `dict`s, because they can't know their keys and value types.

We can do better...