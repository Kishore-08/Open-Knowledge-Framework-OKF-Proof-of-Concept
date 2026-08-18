---
id: fastapi-union-or-anyof-https-fastapi-tiangolo-com-tutorial-extra-mod-bcff185a
type: concept
title: '`Union` or `anyOf`[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#union-or-anyof
  "Permanent link")'
description: You can declare a response to be the `Union` of two or more types, that
  means, that the response would be any of them.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/extra-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## `Union` or `anyOf`[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#union-or-anyof "Permanent link")

You can declare a response to be the `Union` of two or more types, that means, that the response would be any of them.

It will be defined in OpenAPI with `anyOf`.

To do that, use the standard Python type hint [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union):

Note

When defining a [`Union`](https://pydantic.dev/docs/validation/latest/concepts/unions/), include the most specific type first, followed by the less specific type. In the example below, the more specific `PlaneItem` comes before `CarItem` in `Union[PlaneItem, CarItem]`.

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=PlaneItem | CarItem)
async def read_item(item_id: str):
    return items[item_id]
```