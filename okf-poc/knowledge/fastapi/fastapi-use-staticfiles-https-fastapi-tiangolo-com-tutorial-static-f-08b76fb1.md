---
id: fastapi-use-staticfiles-https-fastapi-tiangolo-com-tutorial-static-f-08b76fb1
type: concept
title: Use `StaticFiles`[¶](https://fastapi.tiangolo.com/tutorial/static-files/#use-staticfiles
  "Permanent link")
description: '- Import `StaticFiles`.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/static-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Use `StaticFiles`[¶](https://fastapi.tiangolo.com/tutorial/static-files/#use-staticfiles "Permanent link")

- Import `StaticFiles`.
- "Mount" a `StaticFiles()` instance in a specific path.

Python 3.10+

```
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

Technical Details

You could also use `from starlette.staticfiles import StaticFiles`.

**FastAPI** provides the same `starlette.staticfiles` as `fastapi.staticfiles` just as a convenience for you, the developer. But it actually comes directly from Starlette.