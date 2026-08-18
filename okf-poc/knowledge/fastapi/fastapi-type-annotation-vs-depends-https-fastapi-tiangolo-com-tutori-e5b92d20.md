---
id: fastapi-type-annotation-vs-depends-https-fastapi-tiangolo-com-tutori-e5b92d20
type: concept
title: Type annotation vs `Depends`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#type-annotation-vs-depends
  "Permanent link")
description: 'Notice how we write `CommonQueryParams` twice in the above code:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Type annotation vs `Depends`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#type-annotation-vs-depends "Permanent link")

Notice how we write `CommonQueryParams` twice in the above code:

Python 3.10+Python 3.10+ non-Annotated

```
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

Tip

Prefer to use the `Annotated` version if possible.

```
commons: CommonQueryParams = Depends(CommonQueryParams)
```

The last `CommonQueryParams`, in:

```
... Depends(CommonQueryParams)
```

...is what **FastAPI** will actually use to know what is the dependency.

It is from this one that FastAPI will extract the declared parameters and that is what FastAPI will actually call.

---

In this case, the first `CommonQueryParams`, in:

Python 3.10+Python 3.10+ non-Annotated

```
commons: Annotated[CommonQueryParams, ...
```

Tip

Prefer to use the `Annotated` version if possible.

```
commons: CommonQueryParams ...
```

...doesn't have any special meaning for **FastAPI**. FastAPI won't use it for data conversion, validation, etc. (as it is using the `Depends(CommonQueryParams)` for that).

You could actually write just:

Python 3.10+Python 3.10+ non-Annotated

```
commons: Annotated[Any, Depends(CommonQueryParams)]
```

Tip

Prefer to use the `Annotated` version if possible.

```
commons = Depends(CommonQueryParams)
```

...as in:

Python 3.10+

```
from typing import Annotated, Any

from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: Annotated[Any, Depends(CommonQueryParams)]):
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
async def read_items(commons=Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
```

But declaring the type is encouraged as that way your editor will know what will be passed as the parameter `commons`, and then it can help you with code completion, type checks, etc: