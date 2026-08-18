---
id: fastapi-forbid-extra-query-parameters-https-fastapi-tiangolo-com-tut-a2cdd64f
type: concept
title: Forbid Extra Query Parameters[¶](https://fastapi.tiangolo.com/tutorial/query-param-models/#forbid-extra-query-parameters
  "Permanent link")
description: In some special use cases (probably not very common), you might want
  to **restrict** the query parameters that you want to receive.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-param-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Forbid Extra Query Parameters[¶](https://fastapi.tiangolo.com/tutorial/query-param-models/#forbid-extra-query-parameters "Permanent link")

In some special use cases (probably not very common), you might want to **restrict** the query parameters that you want to receive.

You can use Pydantic's model configuration to `forbid` any `extra` fields:

Python 3.10+

```
from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from typing import Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: FilterParams = Query()):
    return filter_query
```

If a client tries to send some **extra** data in the **query parameters**, they will receive an **error** response.

For example, if the client tries to send a `tool` query parameter with a value of `plumbus`, like:

```
https://example.com/items/?limit=10&tool=plumbus
```

They will receive an **error** response telling them that the query parameter `tool` is not allowed:

```
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["query", "tool"],
            "msg": "Extra inputs are not permitted",
            "input": "plumbus"
        }
    ]
}
```