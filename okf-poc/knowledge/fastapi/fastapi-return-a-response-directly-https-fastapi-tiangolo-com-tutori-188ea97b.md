---
id: fastapi-return-a-response-directly-https-fastapi-tiangolo-com-tutori-188ea97b
type: concept
title: Return a Response Directly[¶](https://fastapi.tiangolo.com/tutorial/response-model/#return-a-response-directly
  "Permanent link")
description: The most common case would be [returning a Response directly as explained
  later in the advanced docs](https://fastapi.tiangolo.com/advanced/response-directly/).
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Return a Response Directly[¶](https://fastapi.tiangolo.com/tutorial/response-model/#return-a-response-directly "Permanent link")

The most common case would be [returning a Response directly as explained later in the advanced docs](https://fastapi.tiangolo.com/advanced/response-directly/).

Python 3.10+

```
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()


@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})
```

This simple case is handled automatically by FastAPI because the return type annotation is the class (or a subclass of) `Response`.

And tools will also be happy because both `RedirectResponse` and `JSONResponse` are subclasses of `Response`, so the type annotation is correct.