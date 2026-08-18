---
id: fastapi-create-your-data-model-https-fastapi-tiangolo-com-tutorial-b-db923f63
type: concept
title: Create your data model[¶](https://fastapi.tiangolo.com/tutorial/body/#create-your-data-model
  "Permanent link")
description: Then you declare your data model as a class that inherits from `BaseModel`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Create your data model[¶](https://fastapi.tiangolo.com/tutorial/body/#create-your-data-model "Permanent link")

Then you declare your data model as a class that inherits from `BaseModel`.

Use standard Python types for all the attributes:

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
```

The same as when declaring query parameters, when a model attribute has a default value, it is not required. Otherwise, it is required. Use `None` to make it just optional.

For example, this model above declares a JSON "`object`" (or Python `dict`) like:

```
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
```

...as `description` and `tax` are optional (with a default value of `None`), this JSON "`object`" would also be valid:

```
{
    "name": "Foo",
    "price": 45.2
}
```