---
id: fastapi-extended-fastapi-app-file-https-fastapi-tiangolo-com-tutoria-459f3498
type: concept
title: Extended **FastAPI** app file[¶](https://fastapi.tiangolo.com/tutorial/testing/#extended-fastapi-app-file
  "Permanent link")
description: 'Let''s continue with the same file structure as before:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/testing/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Extended **FastAPI** app file[¶](https://fastapi.tiangolo.com/tutorial/testing/#extended-fastapi-app-file "Permanent link")

Let's continue with the same file structure as before:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

Let's say that now the file `main.py` with your **FastAPI** app has some other **path operations**.

It has a `GET` operation that could return an error.

It has a `POST` operation that could return several errors.

Both *path operations* require an `X-Token` header.

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

fake_secret_token = "coneofsilence"

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

app = FastAPI()


class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@app.post("/items/")
async def create_item(item: Item, x_token: Annotated[str, Header()]) -> Item:
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=409, detail="Item already exists")
    fake_db[item.id] = item.model_dump()
    return item
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

fake_secret_token = "coneofsilence"

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

app = FastAPI()


class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: str = Header()):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@app.post("/items/")
async def create_item(item: Item, x_token: str = Header()) -> Item:
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=409, detail="Item already exists")
    fake_db[item.id] = item.model_dump()
    return item
```