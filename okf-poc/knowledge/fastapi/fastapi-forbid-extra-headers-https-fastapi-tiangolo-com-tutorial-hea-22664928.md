---
id: fastapi-forbid-extra-headers-https-fastapi-tiangolo-com-tutorial-hea-22664928
type: concept
title: Forbid Extra Headers[¶](https://fastapi.tiangolo.com/tutorial/header-param-models/#forbid-extra-headers
  "Permanent link")
description: In some special use cases (probably not very common), you might want
  to **restrict** the headers that you want to receive.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/header-param-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Forbid Extra Headers[¶](https://fastapi.tiangolo.com/tutorial/header-param-models/#forbid-extra-headers "Permanent link")

In some special use cases (probably not very common), you might want to **restrict** the headers that you want to receive.

You can use Pydantic's model configuration to `forbid` any `extra` fields:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"}

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
    model_config = {"extra": "forbid"}

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: CommonHeaders = Header()):
    return headers
```

If a client tries to send some **extra headers**, they will receive an **error** response.

For example, if the client tries to send a `tool` header with a value of `plumbus`, they will receive an **error** response telling them that the header parameter `tool` is not allowed:

```
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["header", "tool"],
            "msg": "Extra inputs are not permitted",
            "input": "plumbus",
        }
    ]
}
```