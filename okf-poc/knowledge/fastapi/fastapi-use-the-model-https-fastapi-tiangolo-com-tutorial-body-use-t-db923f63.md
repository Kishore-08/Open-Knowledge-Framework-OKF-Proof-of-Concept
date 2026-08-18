---
id: fastapi-use-the-model-https-fastapi-tiangolo-com-tutorial-body-use-t-db923f63
type: concept
title: Use the model[¶](https://fastapi.tiangolo.com/tutorial/body/#use-the-model
  "Permanent link")
description: 'Inside of the function, you can access all the attributes of the model
  object directly:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Use the model[¶](https://fastapi.tiangolo.com/tutorial/body/#use-the-model "Permanent link")

Inside of the function, you can access all the attributes of the model object directly:

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
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
```