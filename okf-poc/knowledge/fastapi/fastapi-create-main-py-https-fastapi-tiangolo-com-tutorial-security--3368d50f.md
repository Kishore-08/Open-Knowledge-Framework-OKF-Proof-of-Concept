---
id: fastapi-create-main-py-https-fastapi-tiangolo-com-tutorial-security--3368d50f
type: concept
title: Create `main.py`[¶](https://fastapi.tiangolo.com/tutorial/security/first-steps/#create-main-py
  "Permanent link")
description: 'Copy the example in a file `main.py`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/first-steps/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Create `main.py`[¶](https://fastapi.tiangolo.com/tutorial/security/first-steps/#create-main-py "Permanent link")

Copy the example in a file `main.py`:

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