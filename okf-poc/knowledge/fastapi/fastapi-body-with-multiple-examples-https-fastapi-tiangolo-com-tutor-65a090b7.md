---
id: fastapi-body-with-multiple-examples-https-fastapi-tiangolo-com-tutor-65a090b7
type: concept
title: '`Body` with multiple `examples`[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#body-with-multiple-examples
  "Permanent link")'
description: 'You can of course also pass multiple `examples`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### `Body` with multiple `examples`[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#body-with-multiple-examples "Permanent link")

You can of course also pass multiple `examples`:

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
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
                {
                    "name": "Bar",
                    "price": "35.4",
                },
                {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            ],
        ),
    ],
):
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
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        examples=[
            {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            },
            {
                "name": "Bar",
                "price": "35.4",
            },
            {
                "name": "Baz",
                "price": "thirty five point four",
            },
        ],
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
```

When you do this, the examples will be part of the internal **JSON Schema** for that body data.

Nevertheless, at the time of writing this, Swagger UI, the tool in charge of showing the docs UI, doesn't support showing multiple examples for the data in **JSON Schema**. But read below for a workaround.