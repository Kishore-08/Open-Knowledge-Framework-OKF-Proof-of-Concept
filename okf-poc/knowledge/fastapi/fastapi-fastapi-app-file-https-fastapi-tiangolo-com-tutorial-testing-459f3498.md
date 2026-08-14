---
id: fastapi-fastapi-app-file-https-fastapi-tiangolo-com-tutorial-testing-459f3498
type: concept
title: '**FastAPI** app file[¶](https://fastapi.tiangolo.com/tutorial/testing/#fastapi-app-file
  "Permanent link")'
description: 'Let''s say you have a file structure as described in [Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/):'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/testing/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### **FastAPI** app file[¶](https://fastapi.tiangolo.com/tutorial/testing/#fastapi-app-file "Permanent link")

Let's say you have a file structure as described in [Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/):

```
.
├── app
│   ├── __init__.py
│   └── main.py
```

In the file `main.py` you have your **FastAPI** app:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
```