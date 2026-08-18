---
id: fastapi-share-annotated-dependencies-https-fastapi-tiangolo-com-tuto-5ffb54cb
type: concept
title: Share `Annotated` dependencies[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#share-annotated-dependencies
  "Permanent link")
description: In the examples above, you see that there's a tiny bit of **code duplication**.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Share `Annotated` dependencies[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#share-annotated-dependencies "Permanent link")

In the examples above, you see that there's a tiny bit of **code duplication**.

When you need to use the `common_parameters()` dependency, you have to write the whole parameter with the type annotation and `Depends()`:

```
commons: Annotated[dict, Depends(common_parameters)]
```

But because we are using `Annotated`, we can store that `Annotated` value in a variable and use it in multiple places:

Python 3.10+

```
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


CommonsDep = Annotated[dict, Depends(common_parameters)]


@app.get("/items/")
async def read_items(commons: CommonsDep):
    return commons


@app.get("/users/")
async def read_users(commons: CommonsDep):
    return commons
```

Tip

This is just standard Python, it's called a "type alias", it's actually not specific to **FastAPI**.

But because **FastAPI** is based on the Python standards, including `Annotated`, you can use this trick in your code. 😎

The dependencies will keep working as expected, and the **best part** is that the **type information will be preserved**, which means that your editor will be able to keep providing you with **autocompletion**, **inline errors**, etc. The same for other tools like `mypy`.

This will be especially useful when you use it in a **large code base** where you use **the same dependencies** over and over again in **many *path operations***.