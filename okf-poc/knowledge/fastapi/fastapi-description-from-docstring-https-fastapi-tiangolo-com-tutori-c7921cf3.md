---
id: fastapi-description-from-docstring-https-fastapi-tiangolo-com-tutori-c7921cf3
type: concept
title: Description from docstring[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#description-from-docstring
  "Permanent link")
description: As descriptions tend to be long and cover multiple lines, you can declare
  the *path operation* description in the function docstring and **FastAPI** will
  read it from there.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Description from docstring[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#description-from-docstring "Permanent link")

As descriptions tend to be long and cover multiple lines, you can declare the *path operation* description in the function docstring and **FastAPI** will read it from there.

You can write [Markdown](https://en.wikipedia.org/wiki/Markdown) in the docstring, it will be interpreted and displayed correctly (taking into account docstring indentation).

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
    tags: set[str] = set()


@app.post("/items/", summary="Create an item")
async def create_item(item: Item) -> Item:
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item
```

It will be used in the interactive docs: