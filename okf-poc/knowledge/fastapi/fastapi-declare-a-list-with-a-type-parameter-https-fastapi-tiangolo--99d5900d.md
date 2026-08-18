---
id: fastapi-declare-a-list-with-a-type-parameter-https-fastapi-tiangolo--99d5900d
type: concept
title: Declare a `list` with a type parameter[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#declare-a-list-with-a-type-parameter
  "Permanent link")
description: To declare types that have type parameters (internal types), like `list`,
  `dict`, `tuple`,
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Declare a `list` with a type parameter[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#declare-a-list-with-a-type-parameter "Permanent link")

To declare types that have type parameters (internal types), like `list`, `dict`, `tuple`,
pass the internal type(s) as "type parameters" using square brackets: `[` and `]`

```
my_list: list[str]
```

That's all standard Python syntax for type declarations.

Use that same standard syntax for model attributes with internal types.

So, in our example, we can make `tags` be specifically a "list of strings":

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


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```