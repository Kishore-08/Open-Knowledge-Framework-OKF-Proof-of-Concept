---
id: fastapi-multiple-path-and-query-parameters-https-fastapi-tiangolo-co-07af7caf
type: concept
title: Multiple path and query parameters[¶](https://fastapi.tiangolo.com/tutorial/query-params/#multiple-path-and-query-parameters
  "Permanent link")
description: You can declare multiple path parameters and query parameters at the
  same time, **FastAPI** knows which is which.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Multiple path and query parameters[¶](https://fastapi.tiangolo.com/tutorial/query-params/#multiple-path-and-query-parameters "Permanent link")

You can declare multiple path parameters and query parameters at the same time, **FastAPI** knows which is which.

And you don't have to declare them in any specific order.

They will be detected by name:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
```