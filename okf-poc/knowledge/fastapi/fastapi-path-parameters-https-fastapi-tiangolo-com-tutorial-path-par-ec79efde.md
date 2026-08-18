---
id: fastapi-path-parameters-https-fastapi-tiangolo-com-tutorial-path-par-ec79efde
type: concept
title: Path Parameters[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-param
description: 'You can declare path "parameters" or "variables" with the same syntax
  used by Python format strings:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Path Parameters[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters "Permanent link")

You can declare path "parameters" or "variables" with the same syntax used by Python format strings:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

The value of the path parameter `item_id` will be passed to your function as the argument `item_id`.

So, if you run this example and go to <http://127.0.0.1:8000/items/foo>, you will see a response of:

```
{"item_id":"foo"}
```