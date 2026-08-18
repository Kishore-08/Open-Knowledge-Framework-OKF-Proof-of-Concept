---
id: fastapi-before-and-after-the-response-https-fastapi-tiangolo-com-tut-6bcf3c71
type: concept
title: Before and after the `response`[¶](https://fastapi.tiangolo.com/tutorial/middleware/#before-and-after-the-response
  "Permanent link")
description: You can add code to be run with the `request`, before any *path operation*
  receives it.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/middleware/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Before and after the `response`[¶](https://fastapi.tiangolo.com/tutorial/middleware/#before-and-after-the-response "Permanent link")

You can add code to be run with the `request`, before any *path operation* receives it.

And also after the `response` is generated, before returning it.

For example, you could add a custom header `X-Process-Time` containing the time in seconds that it took to process the request and generate a response:

Python 3.10+

```
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

Tip

Here we use [`time.perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter) instead of `time.time()` because it can be more precise for these use cases. 🤓