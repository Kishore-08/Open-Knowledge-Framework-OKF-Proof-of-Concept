---
id: fastapi-import-form-https-fastapi-tiangolo-com-tutorial-request-form-16928256
type: concept
title: Import `Form`[¶](https://fastapi.tiangolo.com/tutorial/request-forms/#import-form
  "Permanent link")
description: 'Import `Form` from `fastapi`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-forms/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Import `Form`[¶](https://fastapi.tiangolo.com/tutorial/request-forms/#import-form "Permanent link")

Import `Form` from `fastapi`:

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