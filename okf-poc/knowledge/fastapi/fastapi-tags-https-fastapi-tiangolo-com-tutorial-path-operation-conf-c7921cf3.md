---
id: fastapi-tags-https-fastapi-tiangolo-com-tutorial-path-operation-conf-c7921cf3
type: concept
title: Tags[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#tags
  "Permanent link")
description: 'You can add tags to your *path operation*, pass the parameter `tags`
  with a `list` of `str` (commonly just one `str`):'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Tags[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#tags "Permanent link")

You can add tags to your *path operation*, pass the parameter `tags` with a `list` of `str` (commonly just one `str`):

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/", tags=["items"])
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]
```

They will be added to the OpenAPI schema and used by the automatic documentation interfaces: