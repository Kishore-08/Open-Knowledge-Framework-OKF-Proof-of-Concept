---
id: fastapi-first-dependency-dependable-https-fastapi-tiangolo-com-tutor-7c664f58
type: concept
title: First dependency "dependable"[¶](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#first-dependency-dependable
  "Permanent link")
description: 'You could create a first dependency ("dependable") like:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## First dependency "dependable"[¶](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#first-dependency-dependable "Permanent link")

You could create a first dependency ("dependable") like:

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

It declares an optional query parameter `q` as a `str`, and then it just returns it.

This is quite simple (not very useful), but will help us focus on how the sub-dependencies work.