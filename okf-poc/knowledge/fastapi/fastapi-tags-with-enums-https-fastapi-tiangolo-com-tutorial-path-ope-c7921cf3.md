---
id: fastapi-tags-with-enums-https-fastapi-tiangolo-com-tutorial-path-ope-c7921cf3
type: concept
title: Tags with Enums[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#tags-with-enums
  "Permanent link")
description: If you have a big application, you might end up accumulating **several
  tags**, and you would want to make sure you always use the **same tag** for related
  *path operations*.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Tags with Enums[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#tags-with-enums "Permanent link")

If you have a big application, you might end up accumulating **several tags**, and you would want to make sure you always use the **same tag** for related *path operations*.

In these cases, it could make sense to store the tags in an `Enum`.

**FastAPI** supports that the same way as with plain strings:

Python 3.10+

```
from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class Tags(Enum):
    items = "items"
    users = "users"


@app.get("/items/", tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]


@app.get("/users/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]
```