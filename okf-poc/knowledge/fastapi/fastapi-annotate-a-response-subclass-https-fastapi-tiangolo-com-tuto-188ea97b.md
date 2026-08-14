---
id: fastapi-annotate-a-response-subclass-https-fastapi-tiangolo-com-tuto-188ea97b
type: concept
title: Annotate a Response Subclass[¶](https://fastapi.tiangolo.com/tutorial/response-model/#annotate-a-response-subclass
  "Permanent link")
description: 'You can also use a subclass of `Response` in the type annotation:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Annotate a Response Subclass[¶](https://fastapi.tiangolo.com/tutorial/response-model/#annotate-a-response-subclass "Permanent link")

You can also use a subclass of `Response` in the type annotation:

Python 3.10+

```
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
```

This will also work because `RedirectResponse` is a subclass of `Response`, and FastAPI will automatically handle this simple case.