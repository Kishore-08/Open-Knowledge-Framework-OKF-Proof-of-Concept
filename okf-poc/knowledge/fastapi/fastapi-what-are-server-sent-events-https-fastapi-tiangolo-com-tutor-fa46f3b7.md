---
id: fastapi-what-are-server-sent-events-https-fastapi-tiangolo-com-tutor-fa46f3b7
type: concept
title: What are Server-Sent Events?[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#what-are-server-sent-events
  "Permanent link")
description: SSE is a standard for streaming data from the server to the client over
  HTTP.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/server-sent-events/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## What are Server-Sent Events?[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#what-are-server-sent-events "Permanent link")

SSE is a standard for streaming data from the server to the client over HTTP.

Each event is a small text block with "fields" like `data`, `event`, `id`, and `retry`, separated by blank lines.

It looks like this:

```
data: {"name": "Portal Gun", "price": 999.99}

data: {"name": "Plumbus", "price": 32.99}
```

SSE is commonly used for AI chat streaming, live notifications, logs and observability, and other cases where the server pushes updates to the client.

Tip

If you want to stream binary data, for example video or audio, check the advanced guide: [Stream Data](https://fastapi.tiangolo.com/advanced/stream-data/).