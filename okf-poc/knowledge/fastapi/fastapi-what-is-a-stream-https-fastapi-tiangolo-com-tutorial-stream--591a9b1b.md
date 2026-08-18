---
id: fastapi-what-is-a-stream-https-fastapi-tiangolo-com-tutorial-stream--591a9b1b
type: concept
title: What is a Stream?[¶](https://fastapi.tiangolo.com/tutorial/stream-json-lines/#what-is-a-stream
  "Permanent link")
description: '"**Streaming**" data means that your app will start sending data items
  to the client without waiting for the entire sequence of items to be ready.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/stream-json-lines/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## What is a Stream?[¶](https://fastapi.tiangolo.com/tutorial/stream-json-lines/#what-is-a-stream "Permanent link")

"**Streaming**" data means that your app will start sending data items to the client without waiting for the entire sequence of items to be ready.

So, it will send the first item, the client will receive and start processing it, and you might still be producing the next item.

```
sequenceDiagram
    participant App
    participant Client

    App->>App: Produce Item 1
    App->>Client: Send Item 1
    App->>App: Produce Item 2
    Client->>Client: Process Item 1
    App->>Client: Send Item 2
    App->>App: Produce Item 3
    Client->>Client: Process Item 2
    App->>Client: Send Item 3
    Client->>Client: Process Item 3
    Note over App: Keeps producing...
    Note over Client: Keeps consuming...
```

It could even be an infinite stream, where you keep sending data.