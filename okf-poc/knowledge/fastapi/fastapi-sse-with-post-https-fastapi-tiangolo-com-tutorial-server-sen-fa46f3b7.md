---
id: fastapi-sse-with-post-https-fastapi-tiangolo-com-tutorial-server-sen-fa46f3b7
type: concept
title: SSE with POST[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#sse-with-post
  "Permanent link")
description: SSE works with **any HTTP method**, not just `GET`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/server-sent-events/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## SSE with POST[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#sse-with-post "Permanent link")

SSE works with **any HTTP method**, not just `GET`.

This is useful for protocols like [MCP](https://modelcontextprotocol.io) that stream SSE over `POST`:

Python 3.10+

```
from collections.abc import AsyncIterable

from fastapi import FastAPI
from fastapi.sse import EventSourceResponse, ServerSentEvent
from pydantic import BaseModel

app = FastAPI()


class Prompt(BaseModel):
    text: str


@app.post("/chat/stream", response_class=EventSourceResponse)
async def stream_chat(prompt: Prompt) -> AsyncIterable[ServerSentEvent]:
    words = prompt.text.split()
    for word in words:
        yield ServerSentEvent(data=word, event="token")
    yield ServerSentEvent(raw_data="[DONE]", event="done")
```