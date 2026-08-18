---
id: fastapi-response-model-parameter-https-fastapi-tiangolo-com-tutorial-188ea97b
type: concept
title: '`response_model` Parameter[¶](https://fastapi.tiangolo.com/tutorial/response-model/#response-model-parameter
  "Permanent link")'
description: There are some cases where you need or want to return some data that
  is not exactly what the type declares.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## `response_model` Parameter[¶](https://fastapi.tiangolo.com/tutorial/response-model/#response-model-parameter "Permanent link")

There are some cases where you need or want to return some data that is not exactly what the type declares.

For example, you could want to **return a dictionary** or a database object, but **declare it as a Pydantic model**. This way the Pydantic model would do all the data documentation, validation, etc. for the object that you returned (e.g. a dictionary or database object).

If you added the return type annotation, tools and editors would complain with a (correct) error telling you that your function is returning a type (e.g. a dict) that is different from what you declared (e.g. a Pydantic model).

In those cases, you can use the *path operation decorator* parameter `response_model` instead of the return type.

You can use the `response_model` parameter in any of the *path operations*:

- `@app.get()`
- `@app.post()`
- `@app.put()`
- `@app.delete()`
- etc.

Python 3.10+

```
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]
```

Note

Notice that `response_model` is a parameter of the "decorator" method (`get`, `post`, etc). Not of your *path operation function*, like all the parameters and body.

`response_model` receives the same type you would declare for a Pydantic model field, so, it can be a Pydantic model, but it can also be, e.g. a `list` of Pydantic models, like `List[Item]`.

FastAPI will use this `response_model` to do all the data documentation, validation, etc. and also to **convert and filter the output data** to its type declaration.

Tip

If you have strict type checks in your editor, mypy, etc, you can declare the function return type as `Any`.

That way you tell the editor that you are intentionally returning anything. But FastAPI will still do the data documentation, validation, filtering, etc. with the `response_model`.