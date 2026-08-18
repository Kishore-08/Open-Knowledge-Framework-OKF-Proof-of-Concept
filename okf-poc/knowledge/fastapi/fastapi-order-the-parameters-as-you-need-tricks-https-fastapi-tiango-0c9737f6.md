---
id: fastapi-order-the-parameters-as-you-need-tricks-https-fastapi-tiango-0c9737f6
type: concept
title: Order the parameters as you need, tricks[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#order-the-parameters-as-you-need-tricks
  "Permanent link")
description: Tip
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Order the parameters as you need, tricks[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#order-the-parameters-as-you-need-tricks "Permanent link")

Tip

This is probably not as important or necessary if you use `Annotated`.

Here's a **small trick** that can be handy, but you won't need it often.

If you want to:

- declare the `q` query parameter without a `Query` nor any default value
- declare the path parameter `item_id` using `Path`
- have them in a different order
- not use `Annotated`

...Python has a little special syntax for that.

Pass `*`, as the first parameter of the function.

Python won't do anything with that `*`, but it will know that all the following parameters should be called as keyword arguments (key-value pairs), also known as `kwargs`. Even if they don't have a default value.

Python 3.10+ - non-Annotated

```
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```