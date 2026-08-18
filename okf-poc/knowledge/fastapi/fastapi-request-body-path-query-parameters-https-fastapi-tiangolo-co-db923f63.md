---
id: fastapi-request-body-path-query-parameters-https-fastapi-tiangolo-co-db923f63
type: concept
title: Request body + path + query parameters[¶](https://fastapi.tiangolo.com/tutorial/body/#request-body-path-query-parameters
  "Permanent link")
description: You can also declare **body**, **path** and **query** parameters, all
  at the same time.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Request body + path + query parameters[¶](https://fastapi.tiangolo.com/tutorial/body/#request-body-path-query-parameters "Permanent link")

You can also declare **body**, **path** and **query** parameters, all at the same time.

**FastAPI** will recognize each of them and take the data from the correct place.

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
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
```

The function parameters will be recognized as follows:

- If the parameter is also declared in the **path**, it will be used as a path parameter.
- If the parameter is of a **singular type** (like `int`, `float`, `str`, `bool`, etc) it will be interpreted as a **query** parameter.
- If the parameter is declared to be of the type of a **Pydantic model**, it will be interpreted as a request **body**.

Note

FastAPI will know that the value of `q` is not required because of the default value `= None`.

The `str | None` is not used by FastAPI to determine that the value is not required, it will know it's not required because it has a default value of `= None`.

But adding the type annotations will allow your editor to give you better support and detect errors.