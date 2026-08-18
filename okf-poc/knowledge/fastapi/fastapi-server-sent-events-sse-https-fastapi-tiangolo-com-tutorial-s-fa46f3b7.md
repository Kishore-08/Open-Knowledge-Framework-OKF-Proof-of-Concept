---
id: fastapi-server-sent-events-sse-https-fastapi-tiangolo-com-tutorial-s-fa46f3b7
type: concept
title: Server-Sent Events (SSE)[¶](https://fastapi.tiangolo.com/tutorial/server-sent-ev
description: You can stream data to the client using **Server-Sent Events** (SSE).
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/server-sent-events/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Server-Sent Events (SSE)[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#server-sent-events-sse "Permanent link")

You can stream data to the client using **Server-Sent Events** (SSE).

This is similar to [Stream JSON Lines](https://fastapi.tiangolo.com/tutorial/stream-json-lines/), but uses the `text/event-stream` format, which is supported natively by browsers with the [`EventSource` API](https://developer.mozilla.org/en-US/docs/Web/API/EventSource).

Note

Added in FastAPI 0.135.0.