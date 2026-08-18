---
id: fastapi-raise-exceptions-https-fastapi-tiangolo-com-tutorial-depende-9cbf10cd
type: concept
title: Raise exceptions[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/#raise-exceptions
  "Permanent link")
description: 'These dependencies can `raise` exceptions, the same as normal dependencies:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Raise exceptions[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/#raise-exceptions "Permanent link")

These dependencies can `raise` exceptions, the same as normal dependencies:

Python 3.10+

```
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
```