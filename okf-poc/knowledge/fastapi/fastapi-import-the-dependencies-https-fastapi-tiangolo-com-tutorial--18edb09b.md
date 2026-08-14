---
id: fastapi-import-the-dependencies-https-fastapi-tiangolo-com-tutorial--18edb09b
type: concept
title: Import the dependencies[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-dependencies
  "Permanent link")
description: This code lives in the module `app.routers.items`, the file `app/routers/items.py`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Import the dependencies[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-dependencies "Permanent link")

This code lives in the module `app.routers.items`, the file `app/routers/items.py`.

And we need to get the dependency function from the module `app.dependencies`, the file `app/dependencies.py`.

So we use a relative import with `..` for the dependencies:

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

#### How relative imports work[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#how-relative-imports-work "Permanent link")

Tip

If you know perfectly how imports work, continue to the next section below.

A single dot `.`, like in:

```
from .dependencies import get_token_header
```

would mean:

- Starting in the same package that this module (the file `app/routers/items.py`) lives in (the directory `app/routers/`)...
- find the module `dependencies` (an imaginary file at `app/routers/dependencies.py`)...
- and from it, import the function `get_token_header`.

But that file doesn't exist, our dependencies are in a file at `app/dependencies.py`.

Remember what our app/file structure looks like:

---

The two dots `..`, like in:

```
from ..dependencies import get_token_header
```

mean:

- Starting in the same package that this module (the file `app/routers/items.py`) lives in (the directory `app/routers/`)...
- go to the parent package (the directory `app/`)...
- and in there, find the module `dependencies` (the file at `app/dependencies.py`)...
- and from it, import the function `get_token_header`.

That works correctly! 🎉

---

The same way, if we had used three dots `...`, like in:

```
from ...dependencies import get_token_header
```

that would mean:

- Starting in the same package that this module (the file `app/routers/items.py`) lives in (the directory `app/routers/`)...
- go to the parent package (the directory `app/`)...
- then go to the parent of that package (there's no parent package, `app` is the top level 😱)...
- and in there, find the module `dependencies` (the file at `app/dependencies.py`)...
- and from it, import the function `get_token_header`.

That would refer to some package above `app/`, with its own file `__init__.py`, etc. But we don't have that. So, that would throw an error in our example. 🚨

But now you know how it works, so you can use relative imports in your own apps no matter how complex they are. 🤓