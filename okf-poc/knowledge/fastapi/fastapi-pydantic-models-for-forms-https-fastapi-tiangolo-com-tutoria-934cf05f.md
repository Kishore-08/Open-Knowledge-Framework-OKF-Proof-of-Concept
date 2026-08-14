---
id: fastapi-pydantic-models-for-forms-https-fastapi-tiangolo-com-tutoria-934cf05f
type: concept
title: Pydantic Models for Forms[¶](https://fastapi.tiangolo.com/tutorial/request-form-models/#pydantic-models-for-forms
  "Permanent link")
description: 'You just need to declare a **Pydantic model** with the fields you want
  to receive as **form fields**, and then declare the parameter as `Form`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-form-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Pydantic Models for Forms[¶](https://fastapi.tiangolo.com/tutorial/request-form-models/#pydantic-models-for-forms "Permanent link")

You just need to declare a **Pydantic model** with the fields you want to receive as **form fields**, and then declare the parameter as `Form`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str


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


@app.post("/login/")
async def login(data: FormData = Form()):
    return data
```

**FastAPI** will **extract** the data for **each field** from the **form data** in the request and give you the Pydantic model you defined.

## Check the Docs[¶](https://fastapi.tiangolo.com/tutorial/request-form-models/#check-the-docs "Permanent link")

You can verify it in the docs UI at `/docs`: