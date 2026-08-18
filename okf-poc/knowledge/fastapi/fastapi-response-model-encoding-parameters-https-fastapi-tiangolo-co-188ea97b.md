---
id: fastapi-response-model-encoding-parameters-https-fastapi-tiangolo-co-188ea97b
type: concept
title: Response Model encoding parameters[¶](https://fastapi.tiangolo.com/tutorial/response-model/#response-model-encoding-parameters
  "Permanent link")
description: 'Your response model could have default values, like:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Response Model encoding parameters[¶](https://fastapi.tiangolo.com/tutorial/response-model/#response-model-encoding-parameters "Permanent link")

Your response model could have default values, like:

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
```

- `description: Union[str, None] = None` (or `str | None = None` in Python 3.10) has a default of `None`.
- `tax: float = 10.5` has a default of `10.5`.
- `tags: List[str] = []` has a default of an empty list: `[]`.

but you might want to omit them from the result if they were not actually stored.

For example, if you have models with many optional attributes in a NoSQL database, but you don't want to send very long JSON responses full of default values.