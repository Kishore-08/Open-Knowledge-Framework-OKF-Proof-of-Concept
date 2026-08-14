---
id: fastapi-serversentevent-https-fastapi-tiangolo-com-tutorial-server-s-fa46f3b7
type: concept
title: '`ServerSentEvent`[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#serversentevent
  "Permanent link")'
description: If you need to set SSE fields like `event`, `id`, `retry`, or `comment`,
  you can yield `ServerSentEvent` objects instead of plain data.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/server-sent-events/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## `ServerSentEvent`[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#serversentevent "Permanent link")

If you need to set SSE fields like `event`, `id`, `retry`, or `comment`, you can yield `ServerSentEvent` objects instead of plain data.

Import `ServerSentEvent` from `fastapi.sse`:

Python 3.10+

```
from collections.abc import AsyncIterable

from fastapi import FastAPI
from fastapi.sse import EventSourceResponse, ServerSentEvent
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


items = [
    Item(name="Plumbus", price=32.99),
    Item(name="Portal Gun", price=999.99),
    Item(name="Meeseeks Box", price=49.99),
]


@app.get("/items/stream", response_class=EventSourceResponse)
async def stream_items() -> AsyncIterable[ServerSentEvent]:
    yield ServerSentEvent(comment="stream of item updates")
    for i, item in enumerate(items):
        yield ServerSentEvent(data=item, event="item_update", id=str(i + 1), retry=5000)
```

The `data` field is always encoded as JSON. You can pass any value that can be serialized as JSON, including Pydantic models.