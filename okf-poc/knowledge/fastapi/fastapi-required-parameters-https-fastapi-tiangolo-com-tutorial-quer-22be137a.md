---
id: fastapi-required-parameters-https-fastapi-tiangolo-com-tutorial-quer-22be137a
type: concept
title: Required parameters[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#required-parameters
  "Permanent link")
description: 'When we don''t need to declare more validations or metadata, we can
  make the `q` query parameter required just by not declaring a default value, like:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Required parameters[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#required-parameters "Permanent link")

When we don't need to declare more validations or metadata, we can make the `q` query parameter required just by not declaring a default value, like:

```
q: str
```

instead of:

```
q: str | None = None
```

But we are now declaring it with `Query`, for example like:

```
q: Annotated[str | None, Query(min_length=3)] = None
```

So, when you need to declare a value as required while using `Query`, you can simply not declare a default value:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
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
async def read_items(q: str = Query(min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```