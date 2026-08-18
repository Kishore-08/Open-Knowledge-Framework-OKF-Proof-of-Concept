---
id: fastapi-import-cookie-https-fastapi-tiangolo-com-tutorial-cookie-par-6018d1dd
type: concept
title: Import `Cookie`[¶](https://fastapi.tiangolo.com/tutorial/cookie-params/#import-cookie
  "Permanent link")
description: 'First import `Cookie`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cookie-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Import `Cookie`[¶](https://fastapi.tiangolo.com/tutorial/cookie-params/#import-cookie "Permanent link")

First import `Cookie`:

Python 3.10+

```
from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
```