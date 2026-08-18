---
id: fastapi-add-regular-expressions-https-fastapi-tiangolo-com-tutorial--22be137a
type: concept
title: Add regular expressions[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-regular-expressions
  "Permanent link")
description: 'You can define a regular expression `pattern` that the parameter should
  match:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Add regular expressions[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-regular-expressions "Permanent link")

You can define a regular expression `pattern` that the parameter should match:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
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
async def read_items(
    q: str | None = Query(
        default=None, min_length=3, max_length=50, pattern="^fixedquery$"
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

This specific regular expression pattern checks that the received parameter value:

- `^`: starts with the following characters, doesn't have characters before.
- `fixedquery`: has the exact value `fixedquery`.
- `$`: ends there, doesn't have any more characters after `fixedquery`.

If you feel lost with all these **"regular expression"** ideas, don't worry. They are a hard topic for many people. You can still do a lot of stuff without needing regular expressions yet.

Now you know that whenever you need them you can use them in **FastAPI**.