---
id: fastapi-attributes-with-lists-of-submodels-https-fastapi-tiangolo-co-99d5900d
type: concept
title: Attributes with lists of submodels[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#attributes-with-lists-of-submodels
  "Permanent link")
description: 'You can also use Pydantic models as subtypes of `list`, `set`, etc.:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Attributes with lists of submodels[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#attributes-with-lists-of-submodels "Permanent link")

You can also use Pydantic models as subtypes of `list`, `set`, etc.:

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

This will expect (convert, validate, document, etc.) a JSON body like:

```
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": [
        "rock",
        "metal",
        "bar"
    ],
    "images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
    ]
}
```

Note

Notice how the `images` key now has a list of image objects.