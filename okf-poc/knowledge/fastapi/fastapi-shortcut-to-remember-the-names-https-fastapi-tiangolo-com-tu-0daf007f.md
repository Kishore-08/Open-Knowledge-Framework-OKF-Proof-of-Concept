---
id: fastapi-shortcut-to-remember-the-names-https-fastapi-tiangolo-com-tu-0daf007f
type: concept
title: Shortcut to remember the names[¶](https://fastapi.tiangolo.com/tutorial/response-status-code/#shortcut-to-remember-the-names
  "Permanent link")
description: 'Let''s see the previous example again:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-status-code/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Shortcut to remember the names[¶](https://fastapi.tiangolo.com/tutorial/response-status-code/#shortcut-to-remember-the-names "Permanent link")

Let's see the previous example again:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
```

`201` is the status code for "Created".

But you don't have to memorize what each of these codes mean.

You can use the convenience variables from `fastapi.status`.

Python 3.10+

```
from fastapi import FastAPI, status

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
```

They are just a convenience, they hold the same number, but that way you can use the editor's autocomplete to find them:

Technical Details

You could also use `from starlette import status`.

**FastAPI** provides the same `starlette.status` as `fastapi.status` just as a convenience for you, the developer. But it comes directly from Starlette.