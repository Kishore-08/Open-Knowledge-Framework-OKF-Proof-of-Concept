---
id: fastapi-another-module-with-apirouter-https-fastapi-tiangolo-com-tut-18edb09b
type: concept
title: Another module with `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter
  "Permanent link")
description: Let's say you also have the endpoints dedicated to handling "items" from
  your application in the module at `app/routers/items.py`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Another module with `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter "Permanent link")

Let's say you also have the endpoints dedicated to handling "items" from your application in the module at `app/routers/items.py`.

You have *path operations* for:

- `/items/`
- `/items/{item_id}`

It's all the same structure as with `app/routers/users.py`.

But we want to be smarter and simplify the code a bit.

We know all the *path operations* in this module have the same:

- Path `prefix`: `/items`.
- `tags`: (just one tag: `items`).
- Extra `responses`.
- `dependencies`: they all need that `X-Token` dependency we created.

So, instead of adding all that to each *path operation*, we can add it to the `APIRouter`.

Python 3.8+

app/routers/items.py

```
from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
```

As the path of each *path operation* has to start with `/`, like in:

```
@router.get("/{item_id}")
async def read_item(item_id: str):
    ...
```

...the prefix must not include a final `/`.

So, the prefix in this case is `/items`.

We can also add a list of `tags` and extra `responses` that will be applied to all the *path operations* included in this router.

And we can add a list of `dependencies` that will be added to all the *path operations* in the router and will be executed/solved for each request made to them.

Tip

Note that, much like [dependencies in *path operation decorators*](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/), no value will be passed to your *path operation function*.

The end result is that the item paths are now:

- `/items/`
- `/items/{item_id}`

...as we intended.

- They will be marked with a list of tags that contain a single string `"items"`.
  - These "tags" are especially useful for the automatic interactive documentation systems (using OpenAPI).
- All of them will include the predefined `responses`.
- All these *path operations* will have the list of `dependencies` evaluated/executed before them.
  - If you also declare dependencies in a specific *path operation*, **they will be executed too**.
  - The router dependencies are executed first, then the [`dependencies` in the decorator](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/), and then the normal parameter dependencies.
  - You can also add [`Security` dependencies with `scopes`](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/).

Tip

Having `dependencies` in the `APIRouter` can be used, for example, to require authentication for a whole group of *path operations*. Even if the dependencies are not added individually to each one of them.

Tip

The `prefix`, `tags`, `responses`, and `dependencies` parameters are (as in many other cases) just a feature from **FastAPI** to help you avoid code duplication.