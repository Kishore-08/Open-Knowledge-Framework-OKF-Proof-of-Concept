---
id: fastapi-no-return-type-https-fastapi-tiangolo-com-tutorial-stream-js-591a9b1b
type: concept
title: No Return Type[¶](https://fastapi.tiangolo.com/tutorial/stream-json-lines/#no-return-type
  "Permanent link")
description: You can also omit the return type. FastAPI will then use the [`jsonable_encoder`](https://fastapi.tiangolo.com/tutorial/encoder/)
  to convert the data to something that can be serialized to JSON and th
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/stream-json-lines/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### No Return Type[¶](https://fastapi.tiangolo.com/tutorial/stream-json-lines/#no-return-type "Permanent link")

You can also omit the return type. FastAPI will then use the [`jsonable_encoder`](https://fastapi.tiangolo.com/tutorial/encoder/) to convert the data to something that can be serialized to JSON and then send it as JSON Lines.

Python 3.10+

```
# Code above omitted 👆

@app.get("/items/stream-no-annotation")
async def stream_items_no_annotation():
    for item in items:
        yield item

# Code below omitted 👇
```

👀 Full file preview

Python 3.10+

```
from collections.abc import AsyncIterable, Iterable

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None


items = [
    Item(name="Plumbus", description="A multi-purpose household device."),
    Item(name="Portal Gun", description="A portal opening device."),
    Item(name="Meeseeks Box", description="A box that summons a Meeseeks."),
]


@app.get("/items/stream")
async def stream_items() -> AsyncIterable[Item]:
    for item in items:
        yield item


@app.get("/items/stream-no-async")
def stream_items_no_async() -> Iterable[Item]:
    for item in items:
        yield item


@app.get("/items/stream-no-annotation")
async def stream_items_no_annotation():
    for item in items:
        yield item


@app.get("/items/stream-no-async-no-annotation")
def stream_items_no_async_no_annotation():
    for item in items:
        yield item
```