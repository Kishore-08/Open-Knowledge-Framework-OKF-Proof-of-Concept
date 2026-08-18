---
id: fastapi-technical-details-https-fastapi-tiangolo-com-tutorial-server-fa46f3b7
type: concept
title: Technical Details[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#technical-details
  "Permanent link")
description: FastAPI implements some SSE best practices out of the box.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/server-sent-events/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Technical Details[¶](https://fastapi.tiangolo.com/tutorial/server-sent-events/#technical-details "Permanent link")

FastAPI implements some SSE best practices out of the box.

- Send a **"keep alive" `ping` comment** every 15 seconds when there hasn't been any message, to prevent some proxies from closing the connection, as suggested in the [HTML specification: Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.html#authoring-notes).
- Set the `Cache-Control: no-cache` header to **prevent caching** of the stream.
- Set a special header `X-Accel-Buffering: no` to **prevent buffering** in some proxies like Nginx.

You don't have to do anything about it, it works out of the box. 🤓