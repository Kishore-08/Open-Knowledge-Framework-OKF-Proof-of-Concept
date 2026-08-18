---
id: fastapi-import-pydantic-s-basemodel-https-fastapi-tiangolo-com-tutor-db923f63
type: concept
title: Import Pydantic's `BaseModel`[¶](https://fastapi.tiangolo.com/tutorial/body/#import-pydantics-basemodel
  "Permanent link")
description: 'First, you need to import `BaseModel` from `pydantic`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Import Pydantic's `BaseModel`[¶](https://fastapi.tiangolo.com/tutorial/body/#import-pydantics-basemodel "Permanent link")

First, you need to import `BaseModel` from `pydantic`:

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