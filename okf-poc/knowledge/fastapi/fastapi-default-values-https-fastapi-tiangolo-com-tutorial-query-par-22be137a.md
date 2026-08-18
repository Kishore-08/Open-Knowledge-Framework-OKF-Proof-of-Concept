---
id: fastapi-default-values-https-fastapi-tiangolo-com-tutorial-query-par-22be137a
type: concept
title: Default values[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#default-values
  "Permanent link")
description: You can, of course, use default values other than `None`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Default values[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#default-values "Permanent link")

You can, of course, use default values other than `None`.

Let's say that you want to declare the `q` query parameter to have a `min_length` of `3`, and to have a default value of `"fixedquery"`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
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
async def read_items(q: str = Query(default="fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

Note

Having a default value of any type, including `None`, makes the parameter optional (not required).