---
id: fastapi-import-header-https-fastapi-tiangolo-com-tutorial-header-par-4033bc35
type: concept
title: Import `Header`[¶](https://fastapi.tiangolo.com/tutorial/header-params/#import-header
  "Permanent link")
description: 'First import `Header`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/header-params/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Import `Header`[¶](https://fastapi.tiangolo.com/tutorial/header-params/#import-header "Permanent link")

First import `Header`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}
```