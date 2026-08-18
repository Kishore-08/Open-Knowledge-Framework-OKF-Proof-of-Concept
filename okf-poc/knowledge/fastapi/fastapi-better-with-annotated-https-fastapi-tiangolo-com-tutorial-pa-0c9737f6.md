---
id: fastapi-better-with-annotated-https-fastapi-tiangolo-com-tutorial-pa-0c9737f6
type: concept
title: Better with `Annotated`[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#better-with-annotated
  "Permanent link")
description: Keep in mind that if you use `Annotated`, as you are not using function
  parameter default values, you won't have this problem, and you probably won't need
  to use `*`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Better with `Annotated`[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#better-with-annotated "Permanent link")

Keep in mind that if you use `Annotated`, as you are not using function parameter default values, you won't have this problem, and you probably won't need to use `*`.

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")], q: str
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
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```