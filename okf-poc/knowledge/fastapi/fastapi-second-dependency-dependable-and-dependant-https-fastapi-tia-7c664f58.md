---
id: fastapi-second-dependency-dependable-and-dependant-https-fastapi-tia-7c664f58
type: concept
title: Second dependency, "dependable" and "dependant"[¶](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#second-dependency-dependable-and-dependant
  "Permanent link")
description: 'Then you can create another dependency function (a "dependable") that
  at the same time declares a dependency of its own (so it is a "dependant" too):'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Second dependency, "dependable" and "dependant"[¶](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#second-dependency-dependable-and-dependant "Permanent link")

Then you can create another dependency function (a "dependable") that at the same time declares a dependency of its own (so it is a "dependant" too):

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

Let's focus on the parameters declared:

- Even though this function is a dependency ("dependable") itself, it also declares another dependency (it "depends" on something else).
  - It depends on the `query_extractor`, and assigns the value returned by it to the parameter `q`.
- It also declares an optional `last_query` cookie, as a `str`.
  - If the user didn't provide any query `q`, we use the last query used, which we saved to a cookie before.