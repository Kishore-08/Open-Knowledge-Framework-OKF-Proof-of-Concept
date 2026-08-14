---
id: fastapi-request-body-path-parameters-https-fastapi-tiangolo-com-tuto-db923f63
type: concept
title: Request body + path parameters[¶](https://fastapi.tiangolo.com/tutorial/body/#request-body-path-parameters
  "Permanent link")
description: You can declare path parameters and request body at the same time.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Request body + path parameters[¶](https://fastapi.tiangolo.com/tutorial/body/#request-body-path-parameters "Permanent link")

You can declare path parameters and request body at the same time.

**FastAPI** will recognize that the function parameters that match path parameters should be **taken from the path**, and that function parameters that are declared to be Pydantic models should be **taken from the request body**.

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


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}
```