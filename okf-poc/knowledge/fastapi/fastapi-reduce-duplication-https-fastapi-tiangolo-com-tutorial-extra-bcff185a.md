---
id: fastapi-reduce-duplication-https-fastapi-tiangolo-com-tutorial-extra-bcff185a
type: concept
title: Reduce duplication[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#reduce-duplication
  "Permanent link")
description: Reducing code duplication is one of the core ideas in **FastAPI**.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/extra-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Reduce duplication[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#reduce-duplication "Permanent link")

Reducing code duplication is one of the core ideas in **FastAPI**.

As code duplication increases the chances of bugs, security issues, code desynchronization issues (when you update in one place but not in the others), etc.

And these models are all sharing a lot of the data and duplicating attribute names and types.

We could do better.

We can declare a `UserBase` model that serves as a base for our other models. And then we can make subclasses of that model that inherit its attributes (type declarations, validation, etc).

All the data conversion, validation, documentation, etc. will still work as normally.

That way, we can declare just the differences between the models (with plaintext `password`, with `hashed_password` and without password):

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
```