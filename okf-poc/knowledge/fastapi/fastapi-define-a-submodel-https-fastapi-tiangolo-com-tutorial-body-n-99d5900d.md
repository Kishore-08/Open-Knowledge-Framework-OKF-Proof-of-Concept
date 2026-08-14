---
id: fastapi-define-a-submodel-https-fastapi-tiangolo-com-tutorial-body-n-99d5900d
type: concept
title: Define a submodel[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#define-a-submodel
  "Permanent link")
description: 'For example, we can define an `Image` model:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Define a submodel[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#define-a-submodel "Permanent link")

For example, we can define an `Image` model:

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