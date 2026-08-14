---
id: fastapi-import-httpexception-https-fastapi-tiangolo-com-tutorial-han-9e3b6bbf
type: concept
title: Import `HTTPException`[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#import-httpexception
  "Permanent link")
description: Python 3.10+
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/handling-errors/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Import `HTTPException`[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#import-httpexception "Permanent link")

Python 3.10+

```
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
```