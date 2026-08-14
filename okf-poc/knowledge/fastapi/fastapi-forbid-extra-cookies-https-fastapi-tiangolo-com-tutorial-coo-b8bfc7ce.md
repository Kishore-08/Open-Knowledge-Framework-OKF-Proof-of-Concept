---
id: fastapi-forbid-extra-cookies-https-fastapi-tiangolo-com-tutorial-coo-b8bfc7ce
type: concept
title: Forbid Extra Cookies[¶](https://fastapi.tiangolo.com/tutorial/cookie-param-models/#forbid-extra-cookies
  "Permanent link")
description: In some special use cases (probably not very common), you might want
  to **restrict** the cookies that you want to receive.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cookie-param-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Forbid Extra Cookies[¶](https://fastapi.tiangolo.com/tutorial/cookie-param-models/#forbid-extra-cookies "Permanent link")

In some special use cases (probably not very common), you might want to **restrict** the cookies that you want to receive.

Your API now has the power to control its own cookie consent. 🤪🍪

You can use Pydantic's model configuration to `forbid` any `extra` fields:

Python 3.10+

```
from typing import Annotated

from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Cookies = Cookie()):
    return cookies
```

If a client tries to send some **extra cookies**, they will receive an **error** response.

Poor cookie banners with all their effort to get your consent for the API to reject it. 🍪

For example, if the client tries to send a `santa_tracker` cookie with a value of `good-list-please`, the client will receive an **error** response telling them that the `santa_tracker` cookie is not allowed:

```
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["cookie", "santa_tracker"],
            "msg": "Extra inputs are not permitted",
            "input": "good-list-please",
        }
    ]
}
```

## Summary[¶](https://fastapi.tiangolo.com/tutorial/cookie-param-models/#summary "Permanent link")

You can use **Pydantic models** to declare **cookies** in **FastAPI**. 😎