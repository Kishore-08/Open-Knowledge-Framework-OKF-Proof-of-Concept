---
id: fastapi-return-the-same-input-data-https-fastapi-tiangolo-com-tutori-188ea97b
type: concept
title: Return the same input data[¶](https://fastapi.tiangolo.com/tutorial/response-model/#return-the-same-input-data
  "Permanent link")
description: 'Here we are declaring a `UserIn` model, it will contain a plaintext
  password:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Return the same input data[¶](https://fastapi.tiangolo.com/tutorial/response-model/#return-the-same-input-data "Permanent link")

Here we are declaring a `UserIn` model, it will contain a plaintext password:

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


# Don't do this in production!
@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user
```

Note

To use `EmailStr`, first install [`email-validator`](https://github.com/JoshData/python-email-validator).

Add it to your project:

```
$ uv add email-validator
```

or with:

```
$ uv add "pydantic[email]"
```

And we are using this model to declare our input and the same model to declare our output:

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


# Don't do this in production!
@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user
```

Now, whenever a browser is creating a user with a password, the API will return the same password in the response.

In this case, it might not be a problem, because it's the same user sending the password.

But if we use the same model for another *path operation*, we could be sending our user's passwords to every client.

Danger

Never store the plain password of a user or send it in a response like this, unless you know all the caveats and you know what you are doing.