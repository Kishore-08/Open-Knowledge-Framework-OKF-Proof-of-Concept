---
id: fastapi-call-uvicorn-https-fastapi-tiangolo-com-tutorial-debugging-c-222721d9
type: concept
title: Call `uvicorn`[¶](https://fastapi.tiangolo.com/tutorial/debugging/#call-uvicorn
  "Permanent link")
description: 'In your FastAPI application, import and run `uvicorn` directly:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/debugging/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Call `uvicorn`[¶](https://fastapi.tiangolo.com/tutorial/debugging/#call-uvicorn "Permanent link")

In your FastAPI application, import and run `uvicorn` directly:

Python 3.10+

```
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```