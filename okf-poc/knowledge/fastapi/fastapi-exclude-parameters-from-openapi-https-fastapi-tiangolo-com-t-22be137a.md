---
id: fastapi-exclude-parameters-from-openapi-https-fastapi-tiangolo-com-t-22be137a
type: concept
title: Exclude parameters from OpenAPI[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi
  "Permanent link")
description: 'To exclude a query parameter from the generated OpenAPI schema (and
  thus, from the automatic documentation systems), set the parameter `include_in_schema`
  of `Query` to `False`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Exclude parameters from OpenAPI[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi "Permanent link")

To exclude a query parameter from the generated OpenAPI schema (and thus, from the automatic documentation systems), set the parameter `include_in_schema` of `Query` to `False`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
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
    hidden_query: str | None = Query(default=None, include_in_schema=False),
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
```