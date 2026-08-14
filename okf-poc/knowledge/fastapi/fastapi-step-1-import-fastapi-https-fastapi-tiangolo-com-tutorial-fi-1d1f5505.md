---
id: fastapi-step-1-import-fastapi-https-fastapi-tiangolo-com-tutorial-fi-1d1f5505
type: concept
title: 'Step 1: import `FastAPI`[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-1-import-fastapi
  "Permanent link")'
description: Python 3.10+
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/first-steps/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Step 1: import `FastAPI`[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-1-import-fastapi "Permanent link")

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

`FastAPI` is a Python class that provides all the functionality for your API.

Technical Details

`FastAPI` is a class that inherits directly from `Starlette`.

You can use all the [Starlette](https://starlette.dev/) functionality with `FastAPI` too.