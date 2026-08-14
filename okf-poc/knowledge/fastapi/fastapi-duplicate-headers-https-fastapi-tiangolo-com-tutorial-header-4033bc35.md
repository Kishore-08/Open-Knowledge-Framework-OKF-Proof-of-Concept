---
id: fastapi-duplicate-headers-https-fastapi-tiangolo-com-tutorial-header-4033bc35
type: concept
title: Duplicate headers[¶](https://fastapi.tiangolo.com/tutorial/header-params/#duplicate-headers
  "Permanent link")
description: It is possible to receive duplicate headers. That means, the same header
  with multiple values.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/header-params/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Duplicate headers[¶](https://fastapi.tiangolo.com/tutorial/header-params/#duplicate-headers "Permanent link")

It is possible to receive duplicate headers. That means, the same header with multiple values.

You can define those cases using a list in the type declaration.

You will receive all the values from the duplicate header as a Python `list`.

For example, to declare a header of `X-Token` that can appear more than once, you can write:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: list[str] | None = Header(default=None)):
    return {"X-Token values": x_token}
```

If you communicate with that *path operation* sending two HTTP headers like:

```
X-Token: foo
X-Token: bar
```

The response would be like:

```
{
    "X-Token values": [
        "bar",
        "foo"
    ]
}
```