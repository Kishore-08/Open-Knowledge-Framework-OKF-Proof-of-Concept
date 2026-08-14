---
id: fastapi-docs-urls-https-fastapi-tiangolo-com-tutorial-metadata-docs--afa173ff
type: concept
title: Docs URLs[¶](https://fastapi.tiangolo.com/tutorial/metadata/#docs-urls "Permanent
  link")
description: 'You can configure the two documentation user interfaces included:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/metadata/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Docs URLs[¶](https://fastapi.tiangolo.com/tutorial/metadata/#docs-urls "Permanent link")

You can configure the two documentation user interfaces included:

- **Swagger UI**: served at `/docs`.
  - You can set its URL with the parameter `docs_url`.
  - You can disable it by setting `docs_url=None`.
- **ReDoc**: served at `/redoc`.
  - You can set its URL with the parameter `redoc_url`.
  - You can disable it by setting `redoc_url=None`.

For example, to set Swagger UI to be served at `/documentation` and disable ReDoc:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI(docs_url="/documentation", redoc_url=None)


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]
```