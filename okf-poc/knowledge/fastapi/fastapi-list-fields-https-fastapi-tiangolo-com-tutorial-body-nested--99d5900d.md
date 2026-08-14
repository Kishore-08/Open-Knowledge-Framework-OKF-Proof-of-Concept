---
id: fastapi-list-fields-https-fastapi-tiangolo-com-tutorial-body-nested--99d5900d
type: concept
title: List fields[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#list-fields
  "Permanent link")
description: 'You can define an attribute to be a subtype. For example, a Python `list`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## List fields[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#list-fields "Permanent link")

You can define an attribute to be a subtype. For example, a Python `list`:

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
    tags: list = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

This will make `tags` be a list, although it doesn't declare the type of the elements of the list.