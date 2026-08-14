---
id: fastapi-create-metadata-for-tags-https-fastapi-tiangolo-com-tutorial-afa173ff
type: concept
title: Create metadata for tags[¶](https://fastapi.tiangolo.com/tutorial/metadata/#create-metadata-for-tags
  "Permanent link")
description: Let's try that in an example with tags for `users` and `items`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/metadata/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Create metadata for tags[¶](https://fastapi.tiangolo.com/tutorial/metadata/#create-metadata-for-tags "Permanent link")

Let's try that in an example with tags for `users` and `items`.

Create metadata for your tags and pass it to the `openapi_tags` parameter:

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

Notice that you can use Markdown inside of the descriptions, for example "login" will be shown in bold (**login**) and "fancy" will be shown in italics (*fancy*).

Tip

You don't have to add metadata for all the tags that you use.