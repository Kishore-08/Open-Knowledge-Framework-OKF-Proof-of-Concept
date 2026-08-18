---
id: fastapi-import-depends-https-fastapi-tiangolo-com-tutorial-dependenc-5ffb54cb
type: concept
title: Import `Depends`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#import-depends
  "Permanent link")
description: Python 3.10+
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Import `Depends`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#import-depends "Permanent link")

Python 3.10+

```
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
```