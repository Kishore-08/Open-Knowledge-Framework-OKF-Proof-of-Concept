---
id: fastapi-response-description-https-fastapi-tiangolo-com-tutorial-pat-c7921cf3
type: concept
title: Response description[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#response-description
  "Permanent link")
description: 'You can specify the response description with the parameter `response_description`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Response description[¶](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#response-description "Permanent link")

You can specify the response description with the parameter `response_description`:

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


@app.post(
    "/items/",
    summary="Create an item",
    response_description="The created item",
)
async def create_item(item: Item) -> Item:
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item
```

Note

Notice that `response_description` refers specifically to the response, the `description` refers to the *path operation* in general.

Tip

OpenAPI specifies that each *path operation* requires a response description.

So, if you don't provide one, **FastAPI** will automatically generate one of "Successful response".