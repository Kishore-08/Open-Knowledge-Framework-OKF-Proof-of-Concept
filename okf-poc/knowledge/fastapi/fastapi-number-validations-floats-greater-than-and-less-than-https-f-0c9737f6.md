---
id: fastapi-number-validations-floats-greater-than-and-less-than-https-f-0c9737f6
type: concept
title: 'Number validations: floats, greater than and less than[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-floats-greater-than-and-less-than
  "Permanent link")'
description: Number validations also work for `float` values.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Number validations: floats, greater than and less than[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-floats-greater-than-and-less-than "Permanent link")

Number validations also work for `float` values.

Here's where it becomes important to be able to declare `gt` and not just `ge`. As with it you can require, for example, that a value must be greater than `0`, even if it is less than `1`.

So, `0.5` would be a valid value. But `0.0` or `0` would not.

And the same for `lt`.

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
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
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results
```