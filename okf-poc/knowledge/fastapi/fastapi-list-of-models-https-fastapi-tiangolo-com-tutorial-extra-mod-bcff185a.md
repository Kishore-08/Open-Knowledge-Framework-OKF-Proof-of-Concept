---
id: fastapi-list-of-models-https-fastapi-tiangolo-com-tutorial-extra-mod-bcff185a
type: concept
title: List of models[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#list-of-models
  "Permanent link")
description: The same way, you can declare responses of lists of objects.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/extra-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## List of models[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#list-of-models "Permanent link")

The same way, you can declare responses of lists of objects.

For that, use the standard Python `list`:

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/items/", response_model=list[Item])
async def read_items():
    return items
```