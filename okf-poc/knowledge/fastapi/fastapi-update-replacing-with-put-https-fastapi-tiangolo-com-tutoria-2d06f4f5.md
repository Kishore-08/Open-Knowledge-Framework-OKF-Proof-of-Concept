---
id: fastapi-update-replacing-with-put-https-fastapi-tiangolo-com-tutoria-2d06f4f5
type: concept
title: Update replacing with `PUT`[¶](https://fastapi.tiangolo.com/tutorial/body-updates/#update-replacing-with-put
  "Permanent link")
description: To update an item you can use the [HTTP `PUT`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT)
  operation.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-updates/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Update replacing with `PUT`[¶](https://fastapi.tiangolo.com/tutorial/body-updates/#update-replacing-with-put "Permanent link")

To update an item you can use the [HTTP `PUT`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) operation.

You can use the `jsonable_encoder` to convert the input data to data that can be stored as JSON (e.g. with a NoSQL database). For example, converting `datetime` to `str`.

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


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded
```

`PUT` is used to receive data that should replace the existing data.