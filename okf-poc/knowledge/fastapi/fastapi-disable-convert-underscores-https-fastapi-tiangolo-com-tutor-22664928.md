---
id: fastapi-disable-convert-underscores-https-fastapi-tiangolo-com-tutor-22664928
type: concept
title: Disable Convert Underscores[¶](https://fastapi.tiangolo.com/tutorial/header-param-models/#disable-convert-underscores
  "Permanent link")
description: The same way as with regular header parameters, when you have underscore
  characters in the parameter names, they are **automatically converted to hyphens**.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/header-param-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Disable Convert Underscores[¶](https://fastapi.tiangolo.com/tutorial/header-param-models/#disable-convert-underscores "Permanent link")

The same way as with regular header parameters, when you have underscore characters in the parameter names, they are **automatically converted to hyphens**.

For example, if you have a header parameter `save_data` in the code, the expected HTTP header will be `save-data`, and it will show up like that in the docs.

If for some reason you need to disable this automatic conversion, you can do it as well for Pydantic models for header parameters.

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
async def read_items(
    headers: Annotated[CommonHeaders, Header(convert_underscores=False)],
):
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
async def read_items(headers: CommonHeaders = Header(convert_underscores=False)):
    return headers
```

Warning

Before setting `convert_underscores` to `False`, bear in mind that some HTTP proxies and servers disallow the usage of headers with underscores.

## Summary[¶](https://fastapi.tiangolo.com/tutorial/header-param-models/#summary "Permanent link")

You can use **Pydantic models** to declare **headers** in **FastAPI**. 😎