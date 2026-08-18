---
id: fastapi-openapi-url-https-fastapi-tiangolo-com-tutorial-metadata-ope-afa173ff
type: concept
title: OpenAPI URL[¶](https://fastapi.tiangolo.com/tutorial/metadata/#openapi-url
  "Permanent link")
description: By default, the OpenAPI schema is served at `/openapi.json`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/metadata/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## OpenAPI URL[¶](https://fastapi.tiangolo.com/tutorial/metadata/#openapi-url "Permanent link")

By default, the OpenAPI schema is served at `/openapi.json`.

But you can configure it with the parameter `openapi_url`.

For example, to set it to be served at `/api/v1/openapi.json`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI(openapi_url="/api/v1/openapi.json")


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]
```

If you want to disable the OpenAPI schema completely you can set `openapi_url=None`, that will also disable the documentation user interfaces that use it.