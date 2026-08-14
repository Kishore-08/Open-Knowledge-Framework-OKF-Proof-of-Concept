---
id: fastapi-use-the-dependency-https-fastapi-tiangolo-com-tutorial-depen-7c664f58
type: concept
title: Use the dependency[¶](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#use-the-dependency
  "Permanent link")
description: 'Then we can use the dependency with:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Use the dependency[¶](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#use-the-dependency "Permanent link")

Then we can use the dependency with:

Python 3.10+

```
from typing import Annotated

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None,
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    return {"q_or_cookie": query_or_default}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: str | None = Cookie(default=None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}
```

Note

Notice that we are only declaring one dependency in the *path operation function*, the `query_or_cookie_extractor`.

But **FastAPI** will know that it has to solve `query_extractor` first, to pass the results of that to `query_or_cookie_extractor` while calling it.

```
graph TB

query_extractor(["query_extractor"])
query_or_cookie_extractor(["query_or_cookie_extractor"])

read_query["/items/"]

query_extractor --> query_or_cookie_extractor --> read_query
```