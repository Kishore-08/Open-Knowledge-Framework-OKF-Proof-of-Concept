---
id: fastapi-using-pydantic-s-update-parameter-https-fastapi-tiangolo-com-2d06f4f5
type: concept
title: Using Pydantic's `update` parameter[¶](https://fastapi.tiangolo.com/tutorial/body-updates/#using-pydantics-update-parameter
  "Permanent link")
description: Now, you can create a copy of the existing model using `.model_copy()`,
  and pass the `update` parameter with a `dict` containing the data to update.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-updates/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Using Pydantic's `update` parameter[¶](https://fastapi.tiangolo.com/tutorial/body-updates/#using-pydantics-update-parameter "Permanent link")

Now, you can create a copy of the existing model using `.model_copy()`, and pass the `update` parameter with a `dict` containing the data to update.

Like `stored_item_model.model_copy(update=update_data)`:

Python 3.10+

```
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}")
async def update_item(item_id: str, item: Item) -> Item:
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.model_dump(exclude_unset=True)
    updated_item = stored_item_model.model_copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
```