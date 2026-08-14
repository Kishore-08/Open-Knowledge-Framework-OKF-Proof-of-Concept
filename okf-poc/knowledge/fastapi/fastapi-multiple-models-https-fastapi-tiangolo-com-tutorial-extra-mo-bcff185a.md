---
id: fastapi-multiple-models-https-fastapi-tiangolo-com-tutorial-extra-mo-bcff185a
type: concept
title: Multiple models[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#multiple-models
  "Permanent link")
description: 'Here''s a general idea of what the models could look like with their
  password fields and the places where they are used:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/extra-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Multiple models[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#multiple-models "Permanent link")

Here's a general idea of what the models could look like with their password fields and the places where they are used:

Python 3.10+

```
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


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


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