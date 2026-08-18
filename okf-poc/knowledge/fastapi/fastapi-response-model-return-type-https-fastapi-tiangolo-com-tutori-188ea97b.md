---
id: fastapi-response-model-return-type-https-fastapi-tiangolo-com-tutori-188ea97b
type: concept
title: Response Model - Return Type[¶](https://fastapi.tiangolo.com/tutorial/response-m
description: You can declare the type used for the response by annotating the *path
  operation function* **return type**.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Response Model - Return Type[¶](https://fastapi.tiangolo.com/tutorial/response-model/#response-model-return-type "Permanent link")

You can declare the type used for the response by annotating the *path operation function* **return type**.

You can use **type annotations** the same way you would for input data in function **parameters**, you can use Pydantic models, lists, dictionaries, scalar values like integers, booleans, etc.

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]
```

FastAPI will use this return type to:

- **Validate** the returned data.
  - If the data is invalid (e.g. you are missing a field), it means that *your* app code is broken, not returning what it should, and it will return a server error instead of returning incorrect data. This way you and your clients can be certain that they will receive the data and the data shape expected.
- Add a **JSON Schema** for the response, in the OpenAPI *path operation*.
  - This will be used by the **automatic docs**.
  - It will also be used by automatic client code generation tools.
- **Serialize** the returned data to JSON using Pydantic, which is written in **Rust**, so it will be **much faster**.

But most importantly:

- It will **limit and filter** the output data to what is defined in the return type.
  - This is particularly important for **security**, we'll see more of that below.