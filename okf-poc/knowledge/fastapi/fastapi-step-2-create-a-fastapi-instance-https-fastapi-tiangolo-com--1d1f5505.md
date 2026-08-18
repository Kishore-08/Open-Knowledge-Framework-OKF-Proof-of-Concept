---
id: fastapi-step-2-create-a-fastapi-instance-https-fastapi-tiangolo-com--1d1f5505
type: concept
title: 'Step 2: create a `FastAPI` "instance"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-2-create-a-fastapi-instance
  "Permanent link")'
description: Python 3.10+
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/first-steps/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Step 2: create a `FastAPI` "instance"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-2-create-a-fastapi-instance "Permanent link")

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Here the `app` variable will be an "instance" of the class `FastAPI`.

This will be the main point of interaction to create all your API.