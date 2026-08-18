---
id: fastapi-query-parameter-list-multiple-values-https-fastapi-tiangolo--22be137a
type: concept
title: Query parameter list / multiple values[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-parameter-list-multiple-values
  "Permanent link")
description: When you define a query parameter explicitly with `Query` you can also
  declare it to receive a list of values, or said in another way, to receive multiple
  values.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Query parameter list / multiple values[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-parameter-list-multiple-values "Permanent link")

When you define a query parameter explicitly with `Query` you can also declare it to receive a list of values, or said in another way, to receive multiple values.

For example, to declare a query parameter `q` that can appear multiple times in the URL, you can write:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: list[str] | None = Query(default=None)):
    query_items = {"q": q}
    return query_items
```

Then, with a URL like:

```
http://localhost:8000/items/?q=foo&q=bar
```

you would receive the multiple `q` *query parameters'* values (`foo` and `bar`) in a Python `list` inside your *path operation function*, in the *function parameter* `q`.

So, the response to that URL would be:

```
{
  "q": [
    "foo",
    "bar"
  ]
}
```

Tip

To declare a query parameter with a type of `list`, like in the example above, you need to explicitly use `Query`, otherwise it would be interpreted as a request body.

The interactive API docs will update accordingly, to allow multiple values: