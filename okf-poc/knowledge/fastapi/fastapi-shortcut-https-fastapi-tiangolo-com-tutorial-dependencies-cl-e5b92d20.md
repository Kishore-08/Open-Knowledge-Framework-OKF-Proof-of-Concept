---
id: fastapi-shortcut-https-fastapi-tiangolo-com-tutorial-dependencies-cl-e5b92d20
type: concept
title: Shortcut[¶](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#shortcut
  "Permanent link")
description: 'But you see that we are having some code repetition here, writing `CommonQueryParams`
  twice:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Shortcut[¶](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#shortcut "Permanent link")

But you see that we are having some code repetition here, writing `CommonQueryParams` twice:

Python 3.10+Python 3.10+ non-Annotated

```
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

Tip

Prefer to use the `Annotated` version if possible.

```
commons: CommonQueryParams = Depends(CommonQueryParams)
```

**FastAPI** provides a shortcut for these cases, in where the dependency is *specifically* a class that **FastAPI** will "call" to create an instance of the class itself.

For those specific cases, you can do the following:

Instead of writing:

Python 3.10+Python 3.10+ non-Annotated

```
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

Tip

Prefer to use the `Annotated` version if possible.

```
commons: CommonQueryParams = Depends(CommonQueryParams)
```

...you write:

Python 3.10+Python 3.10+ non-Annotated

```
commons: Annotated[CommonQueryParams, Depends()]
```

Tip

Prefer to use the `Annotated` version if possible.

```
commons: CommonQueryParams = Depends()
```

You declare the dependency as the type of the parameter, and you use `Depends()` without any parameter, instead of having to write the full class *again* inside of `Depends(CommonQueryParams)`.

The same example would then look like:

Python 3.10+

```
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends()):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
```

...and **FastAPI** will know what to do.

Tip

If that seems more confusing than helpful, disregard it, you don't *need* it.

It is just a shortcut. Because **FastAPI** cares about helping you minimize code repetition.