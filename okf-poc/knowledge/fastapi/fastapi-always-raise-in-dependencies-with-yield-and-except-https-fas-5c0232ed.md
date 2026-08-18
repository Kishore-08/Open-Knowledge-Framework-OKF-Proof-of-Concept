---
id: fastapi-always-raise-in-dependencies-with-yield-and-except-https-fas-5c0232ed
type: concept
title: Always `raise` in Dependencies with `yield` and `except`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#always-raise-in-dependencies-with-yield-and-except
  "Permanent link")
description: If you catch an exception in a dependency with `yield`, unless you are
  raising another `HTTPException` or similar, **you should re-raise the original exception**.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Always `raise` in Dependencies with `yield` and `except`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#always-raise-in-dependencies-with-yield-and-except "Permanent link")

If you catch an exception in a dependency with `yield`, unless you are raising another `HTTPException` or similar, **you should re-raise the original exception**.

You can re-raise the same exception using `raise`:

Python 3.10+

```
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


class InternalError(Exception):
    pass


def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("We don't swallow the internal error here, we raise again 😎")
        raise


@app.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only a plumbus here"
        )
    return item_id
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


class InternalError(Exception):
    pass


def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("We don't swallow the internal error here, we raise again 😎")
        raise


@app.get("/items/{item_id}")
def get_item(item_id: str, username: str = Depends(get_username)):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only a plumbus here"
        )
    return item_id
```

Now the client will get the same *HTTP 500 Internal Server Error* response, but the server will have our custom `InternalError` in the logs. 😎