---
id: fastapi-add-some-custom-tags-responses-and-dependencies-https-fastap-18edb09b
type: concept
title: Add some custom `tags`, `responses`, and `dependencies`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#add-some-custom-tags-responses-and-dependencies
  "Permanent link")
description: We are not adding the prefix `/items` nor the `tags=["items"]` to each
  *path operation* because we added them to the `APIRouter`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Add some custom `tags`, `responses`, and `dependencies`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#add-some-custom-tags-responses-and-dependencies "Permanent link")

We are not adding the prefix `/items` nor the `tags=["items"]` to each *path operation* because we added them to the `APIRouter`.

But we can still add *more* `tags` that will be applied to a specific *path operation*, and also some extra `responses` specific to that *path operation*:

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

Tip

This last path operation will have the combination of tags: `["items", "custom"]`.

And it will also have both responses in the documentation, one for `404` and one for `403`.