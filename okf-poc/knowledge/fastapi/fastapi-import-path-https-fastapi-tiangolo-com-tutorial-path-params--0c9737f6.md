---
id: fastapi-import-path-https-fastapi-tiangolo-com-tutorial-path-params--0c9737f6
type: concept
title: Import `Path`[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#import-path
  "Permanent link")
description: 'First, import `Path` from `fastapi`, and import `Annotated`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Import `Path`[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#import-path "Permanent link")

First, import `Path` from `fastapi`, and import `Annotated`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    q: str | None = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

Note

FastAPI added support for `Annotated` (and started recommending it) in version 0.95.0.

If you have an older version, you would get errors when trying to use `Annotated`.

Make sure you [Upgrade the FastAPI version](https://fastapi.tiangolo.com/deployment/versions/#upgrading-the-fastapi-versions) to at least 0.95.1 before using `Annotated`.