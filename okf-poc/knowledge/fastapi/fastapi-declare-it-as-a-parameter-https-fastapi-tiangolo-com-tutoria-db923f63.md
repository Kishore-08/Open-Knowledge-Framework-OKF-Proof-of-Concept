---
id: fastapi-declare-it-as-a-parameter-https-fastapi-tiangolo-com-tutoria-db923f63
type: concept
title: Declare it as a parameter[¶](https://fastapi.tiangolo.com/tutorial/body/#declare-it-as-a-parameter
  "Permanent link")
description: 'To add it to your *path operation*, declare it the same way you declared
  path and query parameters:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Declare it as a parameter[¶](https://fastapi.tiangolo.com/tutorial/body/#declare-it-as-a-parameter "Permanent link")

To add it to your *path operation*, declare it the same way you declared path and query parameters:

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

...and declare its type as the model you created, `Item`.