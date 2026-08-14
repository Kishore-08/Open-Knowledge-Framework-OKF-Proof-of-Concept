---
id: fastapi-resuming-with-last-event-id-https-fastapi-tiangolo-com-tutor-fa46f3b7
type: concept
title: Resuming with `Last-Event-ID`[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#resuming-with-last-event-id
  "Permanent link")
description: When a browser reconnects after a connection drop, it sends the last
  received `id` in the `Last-Event-ID` header.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/server-sent-events/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Resuming with `Last-Event-ID`[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#resuming-with-last-event-id "Permanent link")

When a browser reconnects after a connection drop, it sends the last received `id` in the `Last-Event-ID` header.

You can read it as a header parameter and use it to resume the stream from where the client left off:

Python 3.10+

```
from collections.abc import AsyncIterable
from typing import Annotated

from fastapi import FastAPI, Header
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
async def stream_items(
    last_event_id: Annotated[int | None, Header()] = None,
) -> AsyncIterable[ServerSentEvent]:
    start = last_event_id + 1 if last_event_id is not None else 0
    for i, item in enumerate(items):
        if i < start:
            continue
        yield ServerSentEvent(data=item, id=str(i))
```