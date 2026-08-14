---
id: fastapi-required-can-be-none-https-fastapi-tiangolo-com-tutorial-que-22be137a
type: concept
title: Required, can be `None`[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#required-can-be-none
  "Permanent link")
description: You can declare that a parameter can accept `None`, but that it's still
  required. This would force clients to send a value, even if the value is `None`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Required, can be `None`[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#required-can-be-none "Permanent link")

You can declare that a parameter can accept `None`, but that it's still required. This would force clients to send a value, even if the value is `None`.

To do that, you can declare that `None` is a valid type but simply do not declare a default value:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)]):
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
async def read_items(q: str | None = Query(min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```