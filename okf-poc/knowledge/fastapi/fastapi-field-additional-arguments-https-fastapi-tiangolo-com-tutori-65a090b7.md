---
id: fastapi-field-additional-arguments-https-fastapi-tiangolo-com-tutori-65a090b7
type: concept
title: '`Field` additional arguments[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#field-additional-arguments
  "Permanent link")'
description: 'When using `Field()` with Pydantic models, you can also declare additional
  `examples`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## `Field` additional arguments[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#field-additional-arguments "Permanent link")

When using `Field()` with Pydantic models, you can also declare additional `examples`:

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```