---
id: fastapi-add-query-to-annotated-in-the-q-parameter-https-fastapi-tian-22be137a
type: concept
title: Add `Query` to `Annotated` in the `q` parameter[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-query-to-annotated-in-the-q-parameter
  "Permanent link")
description: 'Now that we have this `Annotated` where we can put more information
  (in this case some additional validation), add `Query` inside of `Annotated`, and
  set the parameter `max_length` to `50`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Add `Query` to `Annotated` in the `q` parameter[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-query-to-annotated-in-the-q-parameter "Permanent link")

Now that we have this `Annotated` where we can put more information (in this case some additional validation), add `Query` inside of `Annotated`, and set the parameter `max_length` to `50`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
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
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

Notice that the default value is still `None`, so the parameter is still optional.

But now, having `Query(max_length=50)` inside of `Annotated`, we are telling FastAPI that we want it to have **additional validation** for this value, we want it to have maximum 50 characters. 😎

Tip

Here we are using `Query()` because this is a **query parameter**. Later we will see others like `Path()`, `Body()`, `Header()`, and `Cookie()`, that also accept the same arguments as `Query()`.

FastAPI will now:

- **Validate** the data making sure that the max length is 50 characters
- Show a **clear error** for the client when the data is not valid
- **Document** the parameter in the OpenAPI schema *path operation* (so it will show up in the **automatic docs UI**)