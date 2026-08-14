---
id: fastapi-use-the-submodel-as-a-type-https-fastapi-tiangolo-com-tutori-99d5900d
type: concept
title: Use the submodel as a type[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#use-the-submodel-as-a-type
  "Permanent link")
description: 'And then we can use it as the type of an attribute:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Use the submodel as a type[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#use-the-submodel-as-a-type "Permanent link")

And then we can use it as the type of an attribute:

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

This would mean that **FastAPI** would expect a body similar to:

```
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
```

Again, doing just that declaration, with **FastAPI** you get:

- Editor support (completion, etc.), even for nested models
- Data conversion
- Data validation
- Automatic documentation