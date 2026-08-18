---
id: fastapi-declare-metadata-https-fastapi-tiangolo-com-tutorial-path-pa-0c9737f6
type: concept
title: Declare metadata[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#declare-metadata
  "Permanent link")
description: You can declare all the same parameters as for `Query`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Declare metadata[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#declare-metadata "Permanent link")

You can declare all the same parameters as for `Query`.

For example, to declare a `title` metadata value for the path parameter `item_id` you can type:

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

A path parameter is always required as it has to be part of the path. Even if you declared it with `None` or set a default value, it would not affect anything, it would still be always required.