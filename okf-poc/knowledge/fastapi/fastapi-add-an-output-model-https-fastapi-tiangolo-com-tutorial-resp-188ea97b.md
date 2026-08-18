---
id: fastapi-add-an-output-model-https-fastapi-tiangolo-com-tutorial-resp-188ea97b
type: concept
title: Add an output model[¶](https://fastapi.tiangolo.com/tutorial/response-model/#add-an-output-model
  "Permanent link")
description: 'We can instead create an input model with the plaintext password and
  an output model without it:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Add an output model[¶](https://fastapi.tiangolo.com/tutorial/response-model/#add-an-output-model "Permanent link")

We can instead create an input model with the plaintext password and an output model without it:

Python 3.10+

```
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
```

Here, even though our *path operation function* is returning the same input user that contains the password:

Python 3.10+

```
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
```

...we declared the `response_model` to be our model `UserOut`, that doesn't include the password:

Python 3.10+

```
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
```

So, **FastAPI** will take care of filtering out all the data that is not declared in the output model (using Pydantic).