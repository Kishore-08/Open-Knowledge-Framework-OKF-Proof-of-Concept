---
id: fastapi-dependencies-https-fastapi-tiangolo-com-tutorial-bigger-appl-18edb09b
type: concept
title: Dependencies[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#dependencies
  "Permanent link")
description: We see that we are going to need some dependencies used in several places
  of the application.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Dependencies[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#dependencies "Permanent link")

We see that we are going to need some dependencies used in several places of the application.

So we put them in their own `dependencies` module (`app/dependencies.py`).

We will now use a simple dependency to read a custom `X-Token` header:

Python 3.10+

app/dependencies.py

```
from typing import Annotated

from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
```

Tip

We are using an invented header to simplify this example.

But in real cases you will get better results using the integrated [Security utilities](https://fastapi.tiangolo.com/tutorial/security/).