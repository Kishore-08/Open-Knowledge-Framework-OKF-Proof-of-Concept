---
id: fastapi-mix-path-query-and-body-parameters-https-fastapi-tiangolo-co-79340250
type: concept
title: Mix `Path`, `Query` and body parameters[¶](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#mix-path-query-and-body-parameters
  "Permanent link")
description: First, of course, you can mix `Path`, `Query` and request body parameter
  declarations freely and **FastAPI** will know what to do.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-multiple-params/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Mix `Path`, `Query` and body parameters[¶](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#mix-path-query-and-body-parameters "Permanent link")

First, of course, you can mix `Path`, `Query` and request body parameter declarations freely and **FastAPI** will know what to do.

And you can also declare body parameters as optional, by setting the default to `None`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
```

Note

Notice that, in this case, the `item` that would be taken from the body is optional. As it has a `None` default value.