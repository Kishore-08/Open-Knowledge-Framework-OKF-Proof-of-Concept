---
id: fastapi-non-async-path-operation-functions-https-fastapi-tiangolo-co-fa46f3b7
type: concept
title: Non-async *path operation functions*[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#non-async-path-operation-functions
  "Permanent link")
description: You can also use regular `def` functions (without `async`), and use `yield`
  the same way.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/server-sent-events/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Non-async *path operation functions*[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#non-async-path-operation-functions "Permanent link")

You can also use regular `def` functions (without `async`), and use `yield` the same way.

FastAPI will make sure it's run correctly so that it doesn't block the event loop.

As in this case the function is not async, the right return type would be `Iterable[Item]`:

Python 3.10+

```
# Code above omitted 👆

@app.get("/items/stream-no-async", response_class=EventSourceResponse)
def sse_items_no_async() -> Iterable[Item]:
    for item in items:
        yield item

# Code below omitted 👇
```

👀 Full file preview

Python 3.10+

```
from collections.abc import AsyncIterable, Iterable

from fastapi import FastAPI
from fastapi.sse import EventSourceResponse
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


@app.get("/items/stream", response_class=EventSourceResponse)
async def sse_items() -> AsyncIterable[Item]:
    for item in items:
        yield item


@app.get("/items/stream-no-async", response_class=EventSourceResponse)
def sse_items_no_async() -> Iterable[Item]:
    for item in items:
        yield item


@app.get("/items/stream-no-annotation", response_class=EventSourceResponse)
async def sse_items_no_annotation():
    for item in items:
        yield item


@app.get("/items/stream-no-async-no-annotation", response_class=EventSourceResponse)
def sse_items_no_async_no_annotation():
    for item in items:
        yield item
```