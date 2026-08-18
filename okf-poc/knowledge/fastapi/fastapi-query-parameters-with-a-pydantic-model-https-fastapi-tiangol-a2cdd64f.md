---
id: fastapi-query-parameters-with-a-pydantic-model-https-fastapi-tiangol-a2cdd64f
type: concept
title: Query Parameters with a Pydantic Model[¶](https://fastapi.tiangolo.com/tutorial/query-param-models/#query-parameters-with-a-pydantic-model
  "Permanent link")
description: 'Declare the **query parameters** that you need in a **Pydantic model**,
  and then declare the parameter as `Query`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-param-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Query Parameters with a Pydantic Model[¶](https://fastapi.tiangolo.com/tutorial/query-param-models/#query-parameters-with-a-pydantic-model "Permanent link")

Declare the **query parameters** that you need in a **Pydantic model**, and then declare the parameter as `Query`:

Python 3.10+

```
from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
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
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: FilterParams = Query()):
    return filter_query
```

**FastAPI** will **extract** the data for **each field** from the **query parameters** in the request and give you the Pydantic model you defined.

## Check the Docs[¶](https://fastapi.tiangolo.com/tutorial/query-param-models/#check-the-docs "Permanent link")

You can see the query parameters in the docs UI at `/docs`: