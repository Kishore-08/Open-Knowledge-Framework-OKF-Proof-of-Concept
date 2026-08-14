---
id: fastapi-disable-response-model-https-fastapi-tiangolo-com-tutorial-r-188ea97b
type: concept
title: Disable Response Model[¶](https://fastapi.tiangolo.com/tutorial/response-model/#disable-response-model
  "Permanent link")
description: Continuing from the example above, you might not want to have the default
  data validation, documentation, filtering, etc. that is performed by FastAPI.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Disable Response Model[¶](https://fastapi.tiangolo.com/tutorial/response-model/#disable-response-model "Permanent link")

Continuing from the example above, you might not want to have the default data validation, documentation, filtering, etc. that is performed by FastAPI.

But you might want to still keep the return type annotation in the function to get the support from tools like editors and type checkers (e.g. mypy).

In this case, you can disable the response model generation by setting `response_model=None`:

Python 3.10+

```
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}
```

This will make FastAPI skip the response model generation and that way you can have any return type annotations you need without it affecting your FastAPI application. 🤓