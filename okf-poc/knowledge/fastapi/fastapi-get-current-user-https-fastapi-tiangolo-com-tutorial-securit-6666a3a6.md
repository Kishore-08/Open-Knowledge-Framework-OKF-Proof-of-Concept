---
id: fastapi-get-current-user-https-fastapi-tiangolo-com-tutorial-securit-6666a3a6
type: concept
title: Get Current User[¶](https://fastapi.tiangolo.com/tutorial/security/get-current-u
description: 'In the previous chapter the security system (which is based on the dependency
  injection system) was giving the *path operation function* a `token` as a `str`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/get-current-user/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Get Current User[¶](https://fastapi.tiangolo.com/tutorial/security/get-current-user/#get-current-user "Permanent link")

In the previous chapter the security system (which is based on the dependency injection system) was giving the *path operation function* a `token` as a `str`:

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

But that is still not that useful.

Let's make it give us the current user.