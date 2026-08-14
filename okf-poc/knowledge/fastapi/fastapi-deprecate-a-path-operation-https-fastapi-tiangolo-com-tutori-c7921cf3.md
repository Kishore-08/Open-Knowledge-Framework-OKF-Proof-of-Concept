---
id: fastapi-deprecate-a-path-operation-https-fastapi-tiangolo-com-tutori-c7921cf3
type: concept
title: Deprecate a *path operation*[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#deprecate-a-path-operation
  "Permanent link")
description: 'If you need to mark a *path operation* as deprecated, but without removing
  it, pass the parameter `deprecated`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Deprecate a *path operation*[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#deprecate-a-path-operation "Permanent link")

If you need to mark a *path operation* as deprecated, but without removing it, pass the parameter `deprecated`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
```

It will be clearly marked as deprecated in the interactive docs:

Check how deprecated and non-deprecated *path operations* look: