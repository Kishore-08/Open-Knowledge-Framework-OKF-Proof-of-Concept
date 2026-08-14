---
id: fastapi-inject-the-current-user-https-fastapi-tiangolo-com-tutorial--6666a3a6
type: concept
title: Inject the current user[¶](https://fastapi.tiangolo.com/tutorial/security/get-current-user/#inject-the-current-user
  "Permanent link")
description: 'So now we can use the same `Depends` with our `get_current_user` in
  the *path operation*:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/get-current-user/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Inject the current user[¶](https://fastapi.tiangolo.com/tutorial/security/get-current-user/#inject-the-current-user "Permanent link")

So now we can use the same `Depends` with our `get_current_user` in the *path operation*:

Python 3.10+

```
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
```

Notice that we declare the type of `current_user` as the Pydantic model `User`.

This will help us inside of the function with all the completion and type checks.

Tip

You might remember that request bodies are also declared with Pydantic models.

Here **FastAPI** won't get confused because you are using `Depends`.

Tip

The way this dependency system is designed allows us to have different dependencies (different "dependables") that all return a `User` model.

We are not restricted to having only one dependency that can return that type of data.