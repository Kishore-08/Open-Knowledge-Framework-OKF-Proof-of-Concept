---
id: fastapi-forbid-extra-form-fields-https-fastapi-tiangolo-com-tutorial-934cf05f
type: concept
title: Forbid Extra Form Fields[¶](https://fastapi.tiangolo.com/tutorial/request-form-models/#forbid-extra-form-fields
  "Permanent link")
description: In some special use cases (probably not very common), you might want
  to **restrict** the form fields to only those declared in the Pydantic model. And
  **forbid** any **extra** fields.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-form-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Forbid Extra Form Fields[¶](https://fastapi.tiangolo.com/tutorial/request-form-models/#forbid-extra-form-fields "Permanent link")

In some special use cases (probably not very common), you might want to **restrict** the form fields to only those declared in the Pydantic model. And **forbid** any **extra** fields.

Note

This is supported since FastAPI version `0.114.0`. 🤓

You can use Pydantic's model configuration to `forbid` any `extra` fields:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}


@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}


@app.post("/login/")
async def login(data: FormData = Form()):
    return data
```

If a client tries to send some extra data, they will receive an **error** response.

For example, if the client tries to send the form fields:

- `username`: `Rick`
- `password`: `Portal Gun`
- `extra`: `Mr. Poopybutthole`

They will receive an error response telling them that the field `extra` is not allowed:

```
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["body", "extra"],
            "msg": "Extra inputs are not permitted",
            "input": "Mr. Poopybutthole"
        }
    ]
}
```

## Summary[¶](https://fastapi.tiangolo.com/tutorial/request-form-models/#summary "Permanent link")

You can use Pydantic models to declare form fields in FastAPI. 😎