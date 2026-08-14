---
id: fastapi-response-status-code-https-fastapi-tiangolo-com-tutorial-pat-c7921cf3
type: concept
title: Response Status Code[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#response-status-code
  "Permanent link")
description: You can define the (HTTP) `status_code` to be used in the response of
  your *path operation*.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Response Status Code[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#response-status-code "Permanent link")

You can define the (HTTP) `status_code` to be used in the response of your *path operation*.

You can pass directly the `int` code, like `404`.

But if you don't remember what each number code is for, you can use the shortcut constants in `status`:

Python 3.10+

```
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item) -> Item:
    return item
```

That status code will be used in the response and will be added to the OpenAPI schema.

Technical Details

You could also use `from starlette import status`.

**FastAPI** provides the same `starlette.status` as `fastapi.status` just as a convenience for you, the developer. But it comes directly from Starlette.