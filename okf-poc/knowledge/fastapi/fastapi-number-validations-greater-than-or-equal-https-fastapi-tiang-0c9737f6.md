---
id: fastapi-number-validations-greater-than-or-equal-https-fastapi-tiang-0c9737f6
type: concept
title: 'Number validations: greater than or equal[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-or-equal
  "Permanent link")'
description: With `Query` and `Path` (and others you'll see later) you can declare
  number constraints.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Number validations: greater than or equal[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-or-equal "Permanent link")

With `Query` and `Path` (and others you'll see later) you can declare number constraints.

Here, with `ge=1`, `item_id` will need to be an integer number "`g`reater than or `e`qual" to `1`.

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
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
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```