---
id: fastapi-multiple-body-params-and-query-https-fastapi-tiangolo-com-tu-79340250
type: concept
title: Multiple body params and query[¶](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#multiple-body-params-and-query
  "Permanent link")
description: Of course, you can also declare additional query parameters whenever
  you need, additional to any body parameters.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-multiple-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Multiple body params and query[¶](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#multiple-body-params-and-query "Permanent link")

Of course, you can also declare additional query parameters whenever you need, additional to any body parameters.

As, by default, singular values are interpreted as query parameters, you don't have to explicitly add a `Query`, you can just do:

```
q: str | None = None
```

For example:

Python 3.10+

```
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(gt=0),
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
```

Note

`Body` also has all the same extra validation and metadata parameters as `Query`, `Path` and others you will see later.