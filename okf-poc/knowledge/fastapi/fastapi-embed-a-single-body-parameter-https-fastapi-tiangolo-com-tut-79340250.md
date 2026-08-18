---
id: fastapi-embed-a-single-body-parameter-https-fastapi-tiangolo-com-tut-79340250
type: concept
title: Embed a single body parameter[¶](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter
  "Permanent link")
description: Let's say you only have a single `item` body parameter from a Pydantic
  model `Item`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-multiple-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Embed a single body parameter[¶](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter "Permanent link")

Let's say you only have a single `item` body parameter from a Pydantic model `Item`.

By default, **FastAPI** will then expect its body directly.

But if you want it to expect a JSON with a key `item` and inside of it the model contents, as it does when you declare extra body parameters, you can use the special `Body` parameter `embed`:

```
item: Annotated[Item, Body(embed=True)]
```

as in:

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


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
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


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
```

In this case **FastAPI** will expect a body like:

```
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
```

instead of:

```
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```