---
id: fastapi-define-form-parameters-https-fastapi-tiangolo-com-tutorial-r-16928256
type: concept
title: Define `Form` parameters[¶](https://fastapi.tiangolo.com/tutorial/request-forms/#define-form-parameters
  "Permanent link")
description: 'Create form parameters the same way you would for `Body` or `Query`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-forms/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Define `Form` parameters[¶](https://fastapi.tiangolo.com/tutorial/request-forms/#define-form-parameters "Permanent link")

Create form parameters the same way you would for `Body` or `Query`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
```

For example, in one of the ways the OAuth2 specification can be used (called "password flow") it is required to send a `username` and `password` as form fields.

The spec requires the fields to be exactly named `username` and `password`, and to be sent as form fields, not JSON.

With `Form` you can declare the same configurations as with `Body` (and `Query`, `Path`, `Cookie`), including validation, examples, an alias (e.g. `user-name` instead of `username`), etc.

Note

`Form` is a class that inherits directly from `Body`.

Tip

To declare form bodies, you need to use `Form` explicitly, because without it the parameters would be interpreted as query parameters or body (JSON) parameters.