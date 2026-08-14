---
id: fastapi-set-types-https-fastapi-tiangolo-com-tutorial-body-nested-mo-99d5900d
type: concept
title: Set types[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#set-types
  "Permanent link")
description: But then we think about it, and realize that tags shouldn't repeat, they
  would probably be unique strings.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Set types[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#set-types "Permanent link")

But then we think about it, and realize that tags shouldn't repeat, they would probably be unique strings.

And Python has a special data type for sets of unique items, the `set`.

Then we can declare `tags` as a set of strings:

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
    tags: set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

With this, even if you receive a request with duplicate data, it will be converted to a set of unique items.

And whenever you output that data, even if the source had duplicates, it will be output as a set of unique items.

And it will be annotated / documented accordingly too.