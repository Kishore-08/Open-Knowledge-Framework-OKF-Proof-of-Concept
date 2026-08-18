---
id: fastapi-optional-parameters-https-fastapi-tiangolo-com-tutorial-quer-07af7caf
type: concept
title: Optional parameters[¶](https://fastapi.tiangolo.com/tutorial/query-params/#optional-parameters
  "Permanent link")
description: 'The same way, you can declare optional query parameters, by setting
  their default to `None`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Optional parameters[¶](https://fastapi.tiangolo.com/tutorial/query-params/#optional-parameters "Permanent link")

The same way, you can declare optional query parameters, by setting their default to `None`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```

In this case, the function parameter `q` will be optional, and will be `None` by default.

Tip

Also notice that **FastAPI** is smart enough to notice that the path parameter `item_id` is a path parameter and `q` is not, so, it's a query parameter.