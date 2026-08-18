---
id: fastapi-order-the-parameters-as-you-need-https-fastapi-tiangolo-com--0c9737f6
type: concept
title: Order the parameters as you need[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#order-the-parameters-as-you-need
  "Permanent link")
description: Tip
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Order the parameters as you need[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#order-the-parameters-as-you-need "Permanent link")

Tip

This is probably not as important or necessary if you use `Annotated`.

Let's say that you want to declare the query parameter `q` as a required `str`.

And you don't need to declare anything else for that parameter, so you don't really need to use `Query`.

But you still need to use `Path` for the `item_id` path parameter. And you don't want to use `Annotated` for some reason.

Python will complain if you put a value with a "default" before a value that doesn't have a "default".

But you can re-order them, and have the value without a default (the query parameter `q`) first.

It doesn't matter for **FastAPI**. It will detect the parameters by their names, types and default declarations (`Query`, `Path`, etc), it doesn't care about the order.

So, you can declare your function as:

Python 3.10+ - non-Annotated

```
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

But keep in mind that if you use `Annotated`, you won't have this problem, it won't matter as you're not using the function parameter default values for `Query()` or `Path()`.

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```