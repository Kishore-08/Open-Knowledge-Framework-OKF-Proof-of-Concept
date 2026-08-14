---
id: fastapi-declare-header-parameters-https-fastapi-tiangolo-com-tutoria-4033bc35
type: concept
title: Declare `Header` parameters[¶](https://fastapi.tiangolo.com/tutorial/header-params/#declare-header-parameters
  "Permanent link")
description: Then declare the header parameters using the same structure as with `Path`,
  `Query` and `Cookie`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/header-params/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Declare `Header` parameters[¶](https://fastapi.tiangolo.com/tutorial/header-params/#declare-header-parameters "Permanent link")

Then declare the header parameters using the same structure as with `Path`, `Query` and `Cookie`.

You can define the default value as well as all the extra validation or annotation parameters:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}
```

Technical Details

`Header` is a "sister" class of `Path`, `Query` and `Cookie`. It also inherits from the same common `Param` class.

But remember that when you import `Query`, `Path`, `Header`, and others from `fastapi`, those are actually functions that return special classes.

Note

To declare headers, you need to use `Header`, because otherwise the parameters would be interpreted as query parameters.