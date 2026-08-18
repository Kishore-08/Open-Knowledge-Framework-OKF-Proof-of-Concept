---
id: fastapi-cookies-with-a-pydantic-model-https-fastapi-tiangolo-com-tut-b8bfc7ce
type: concept
title: Cookies with a Pydantic Model[¶](https://fastapi.tiangolo.com/tutorial/cookie-param-models/#cookies-with-a-pydantic-model
  "Permanent link")
description: 'Declare the **cookie** parameters that you need in a **Pydantic model**,
  and then declare the parameter as `Cookie`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cookie-param-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Cookies with a Pydantic Model[¶](https://fastapi.tiangolo.com/tutorial/cookie-param-models/#cookies-with-a-pydantic-model "Permanent link")

Declare the **cookie** parameters that you need in a **Pydantic model**, and then declare the parameter as `Cookie`:

Python 3.10+

```
from typing import Annotated

from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
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
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Cookies = Cookie()):
    return cookies
```

**FastAPI** will **extract** the data for **each field** from the **cookies** received in the request and give you the Pydantic model you defined.