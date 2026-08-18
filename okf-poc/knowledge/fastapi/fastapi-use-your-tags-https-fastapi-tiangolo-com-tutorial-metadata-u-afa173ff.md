---
id: fastapi-use-your-tags-https-fastapi-tiangolo-com-tutorial-metadata-u-afa173ff
type: concept
title: Use your tags[¶](https://fastapi.tiangolo.com/tutorial/metadata/#use-your-tags
  "Permanent link")
description: 'Use the `tags` parameter with your *path operations* (and `APIRouter`s)
  to assign them to different tags:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/metadata/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Use your tags[¶](https://fastapi.tiangolo.com/tutorial/metadata/#use-your-tags "Permanent link")

Use the `tags` parameter with your *path operations* (and `APIRouter`s) to assign them to different tags:

Python 3.10+

```
from fastapi import FastAPI

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(openapi_tags=tags_metadata)


@app.get("/users/", tags=["users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]


@app.get("/items/", tags=["items"])
async def get_items():
    return [{"name": "wand"}, {"name": "flying broom"}]
```

Note

Read more about tags in [Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#tags).

### Check the docs[¶](https://fastapi.tiangolo.com/tutorial/metadata/#check-the-docs "Permanent link")

Now, if you check the docs, they will show all the additional metadata: