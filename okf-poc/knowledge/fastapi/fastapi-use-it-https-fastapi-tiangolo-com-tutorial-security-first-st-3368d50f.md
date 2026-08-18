---
id: fastapi-use-it-https-fastapi-tiangolo-com-tutorial-security-first-st-3368d50f
type: concept
title: Use it[¶](https://fastapi.tiangolo.com/tutorial/security/first-steps/#use-it
  "Permanent link")
description: Now you can pass that `oauth2_scheme` in a dependency with `Depends`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/first-steps/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Use it[¶](https://fastapi.tiangolo.com/tutorial/security/first-steps/#use-it "Permanent link")

Now you can pass that `oauth2_scheme` in a dependency with `Depends`.

Python 3.10+

```
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

This dependency will provide a `str` that is assigned to the parameter `token` of the *path operation function*.

**FastAPI** will know that it can use this dependency to define a "security scheme" in the OpenAPI schema (and the automatic API docs).

Technical Details

**FastAPI** will know that it can use the class `OAuth2PasswordBearer` (declared in a dependency) to define the security scheme in OpenAPI because it inherits from `fastapi.security.oauth2.OAuth2`, which in turn inherits from `fastapi.security.base.SecurityBase`.

All the security utilities that integrate with OpenAPI (and the automatic API docs) inherit from `SecurityBase`, that's how **FastAPI** can know how to integrate them in OpenAPI.