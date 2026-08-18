---
id: fastapi-return-type-and-data-filtering-https-fastapi-tiangolo-com-tu-188ea97b
type: concept
title: Return Type and Data Filtering[¶](https://fastapi.tiangolo.com/tutorial/response-model/#return-type-and-data-filtering
  "Permanent link")
description: Let's continue from the previous example. We wanted to **annotate the
  function with one type**, but we wanted to be able to return from the function something
  that actually includes **more data**.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Return Type and Data Filtering[¶](https://fastapi.tiangolo.com/tutorial/response-model/#return-type-and-data-filtering "Permanent link")

Let's continue from the previous example. We wanted to **annotate the function with one type**, but we wanted to be able to return from the function something that actually includes **more data**.

We want FastAPI to keep **filtering** the data using the response model. So that even though the function returns more data, the response will only include the fields declared in the response model.

In the previous example, because the classes were different, we had to use the `response_model` parameter. But that also means that we don't get the support from the editor and tools checking the function return type.

But in most of the cases where we need to do something like this, we want the model just to **filter/remove** some of the data as in this example.

And in those cases, we can use classes and inheritance to take advantage of function **type annotations** to get better support in the editor and tools, and still get the FastAPI **data filtering**.

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user
```

With this, we get tooling support, from editors and mypy as this code is correct in terms of types, but we also get the data filtering from FastAPI.

How does this work? Let's check that out. 🤓