---
id: fastapi-automatic-conversion-https-fastapi-tiangolo-com-tutorial-hea-4033bc35
type: concept
title: Automatic conversion[¶](https://fastapi.tiangolo.com/tutorial/header-params/#automatic-conversion
  "Permanent link")
description: '`Header` has a little extra functionality on top of what `Path`, `Query`
  and `Cookie` provide.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/header-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Automatic conversion[¶](https://fastapi.tiangolo.com/tutorial/header-params/#automatic-conversion "Permanent link")

`Header` has a little extra functionality on top of what `Path`, `Query` and `Cookie` provide.

Most of the standard headers are separated by a "hyphen" character, also known as the "minus symbol" (`-`).

But a variable like `user-agent` is invalid in Python.

So, by default, `Header` will convert the parameter names characters from underscore (`_`) to hyphen (`-`) to extract and document the headers.

Also, HTTP headers are case-insensitive, so, you can declare them with standard Python style (also known as "snake\_case").

So, you can use `user_agent` as you normally would in Python code, instead of needing to capitalize the first letters as `User_Agent` or something similar.

If for some reason you need to disable automatic conversion of underscores to hyphens, set the parameter `convert_underscores` of `Header` to `False`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
):
    return {"strange_header": strange_header}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    strange_header: str | None = Header(default=None, convert_underscores=False),
):
    return {"strange_header": strange_header}
```

Warning

Before setting `convert_underscores` to `False`, bear in mind that some HTTP proxies and servers disallow the usage of headers with underscores.