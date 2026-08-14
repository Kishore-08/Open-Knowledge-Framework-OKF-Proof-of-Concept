---
id: fastapi-step-5-return-the-content-https-fastapi-tiangolo-com-tutoria-1d1f5505
type: concept
title: 'Step 5: return the content[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-5-return-the-content
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

### Step 5: return the content[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-5-return-the-content "Permanent link")

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

You can return a `dict`, `list`, singular values as `str`, `int`, etc.

You can also return Pydantic models (you'll see more about that later).

There are many other objects and models that will be automatically converted to JSON (including ORMs, etc). Try using your favorite ones, it's highly probable that they are already supported.