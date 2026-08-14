---
id: fastapi-add-more-validations-https-fastapi-tiangolo-com-tutorial-que-22be137a
type: concept
title: Add more validations[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-more-validations
  "Permanent link")
description: 'You can also add a parameter `min_length`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Add more validations[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-more-validations "Permanent link")

You can also add a parameter `min_length`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = Query(default=None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```