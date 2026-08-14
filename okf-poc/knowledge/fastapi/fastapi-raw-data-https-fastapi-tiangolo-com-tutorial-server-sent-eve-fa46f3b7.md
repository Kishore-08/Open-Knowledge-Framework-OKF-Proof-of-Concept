---
id: fastapi-raw-data-https-fastapi-tiangolo-com-tutorial-server-sent-eve-fa46f3b7
type: concept
title: Raw Data[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#raw-data
  "Permanent link")
description: If you need to send data **without** JSON encoding, use `raw_data` instead
  of `data`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/server-sent-events/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Raw Data[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#raw-data "Permanent link")

If you need to send data **without** JSON encoding, use `raw_data` instead of `data`.

This is useful for sending pre-formatted text, log lines, or special "sentinel" values like `[DONE]`.

Python 3.10+

```
from collections.abc import AsyncIterable

from fastapi import FastAPI
from fastapi.sse import EventSourceResponse, ServerSentEvent

app = FastAPI()


@app.get("/logs/stream", response_class=EventSourceResponse)
async def stream_logs() -> AsyncIterable[ServerSentEvent]:
    logs = [
        "2025-01-01 INFO  Application started",
        "2025-01-01 DEBUG Connected to database",
        "2025-01-01 WARN  High memory usage detected",
    ]
    for log_line in logs:
        yield ServerSentEvent(raw_data=log_line)
```

Note

`data` and `raw_data` are mutually exclusive. You can only set one of them on each `ServerSentEvent`.