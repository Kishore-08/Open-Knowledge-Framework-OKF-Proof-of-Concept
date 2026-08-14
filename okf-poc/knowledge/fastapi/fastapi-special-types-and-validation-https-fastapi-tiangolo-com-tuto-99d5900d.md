---
id: fastapi-special-types-and-validation-https-fastapi-tiangolo-com-tuto-99d5900d
type: concept
title: Special types and validation[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#special-types-and-validation
  "Permanent link")
description: Apart from normal singular types like `str`, `int`, `float`, etc. you
  can use more complex singular types that inherit from `str`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Special types and validation[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#special-types-and-validation "Permanent link")

Apart from normal singular types like `str`, `int`, `float`, etc. you can use more complex singular types that inherit from `str`.

To see all the options you have, check out [Pydantic's Type Overview](https://pydantic.dev/docs/validation/latest/concepts/types/). You will see some examples in the next chapter.

For example, as in the `Image` model we have a `url` field, we can declare it to be an instance of Pydantic's `HttpUrl` instead of a `str`:

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
    image: Image | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

The string will be checked to be a valid URL, and documented in JSON Schema / OpenAPI as such.