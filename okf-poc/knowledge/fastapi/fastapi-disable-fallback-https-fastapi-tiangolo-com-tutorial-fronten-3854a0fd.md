---
id: fastapi-disable-fallback-https-fastapi-tiangolo-com-tutorial-fronten-3854a0fd
type: concept
title: Disable Fallback[¶](https://fastapi.tiangolo.com/tutorial/frontend/#disable-fallback
  "Permanent link")
description: 'If you don''t want to serve a fallback file for missing frontend paths,
  use `fallback=None`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/frontend/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Disable Fallback[¶](https://fastapi.tiangolo.com/tutorial/frontend/#disable-fallback "Permanent link")

If you don't want to serve a fallback file for missing frontend paths, use `fallback=None`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

app.frontend("/", directory="dist", fallback=None)
```

Then missing frontend paths return the normal `404`.