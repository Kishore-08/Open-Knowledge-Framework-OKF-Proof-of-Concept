---
id: fastapi-header-parameters-with-a-pydantic-model-https-fastapi-tiango-22664928
type: concept
title: Header Parameters with a Pydantic Model[¶](https://fastapi.tiangolo.com/tutorial/header-param-models/#header-parameters-with-a-pydantic-model
  "Permanent link")
description: 'Declare the **header parameters** that you need in a **Pydantic model**,
  and then declare the parameter as `Header`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/header-param-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Header Parameters with a Pydantic Model[¶](https://fastapi.tiangolo.com/tutorial/header-param-models/#header-parameters-with-a-pydantic-model "Permanent link")

Declare the **header parameters** that you need in a **Pydantic model**, and then declare the parameter as `Header`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: CommonHeaders = Header()):
    return headers
```

**FastAPI** will **extract** the data for **each field** from the **headers** in the request and give you the Pydantic model you defined.

## Check the Docs[¶](https://fastapi.tiangolo.com/tutorial/header-param-models/#check-the-docs "Permanent link")

You can see the required headers in the docs UI at `/docs`: