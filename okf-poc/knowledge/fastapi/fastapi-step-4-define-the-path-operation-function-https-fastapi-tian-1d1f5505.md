---
id: fastapi-step-4-define-the-path-operation-function-https-fastapi-tian-1d1f5505
type: concept
title: 'Step 4: define the **path operation function**[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-4-define-the-path-operation-function
  "Permanent link")'
description: 'This is our "**path operation function**":'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/first-steps/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Step 4: define the **path operation function**[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-4-define-the-path-operation-function "Permanent link")

This is our "**path operation function**":

- **path**: is `/`.
- **operation**: is `get`.
- **function**: is the function below the "decorator" (below `@app.get("/")`).

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

This is a Python function.

It will be called by **FastAPI** whenever it receives a request to the URL "`/`" using a `GET` operation.

In this case, it is an `async` function.

---

You could also define it as a normal function instead of `async def`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
```

Note

If you don't know the difference, check the [Async: *"In a hurry?"*](https://fastapi.tiangolo.com/async/#in-a-hurry).