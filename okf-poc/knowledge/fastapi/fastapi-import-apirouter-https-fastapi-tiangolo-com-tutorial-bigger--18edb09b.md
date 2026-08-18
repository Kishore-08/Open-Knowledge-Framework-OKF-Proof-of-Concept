---
id: fastapi-import-apirouter-https-fastapi-tiangolo-com-tutorial-bigger--18edb09b
type: concept
title: Import `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-apirouter
  "Permanent link")
description: 'You import it and create an "instance" the same way you would with the
  class `FastAPI`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Import `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-apirouter "Permanent link")

You import it and create an "instance" the same way you would with the class `FastAPI`:

Python 3.8+

app/routers/users.py

```
from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
```