---
id: fastapi-deeply-nested-models-https-fastapi-tiangolo-com-tutorial-bod-99d5900d
type: concept
title: Deeply nested models[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#deeply-nested-models
  "Permanent link")
description: 'You can define arbitrarily deeply nested models:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Deeply nested models[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#deeply-nested-models "Permanent link")

You can define arbitrarily deeply nested models:

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


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer
```

Note

Notice how `Offer` has a list of `Item`s, which in turn have an optional list of `Image`s