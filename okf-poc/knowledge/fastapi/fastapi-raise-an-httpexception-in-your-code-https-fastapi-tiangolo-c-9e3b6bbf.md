---
id: fastapi-raise-an-httpexception-in-your-code-https-fastapi-tiangolo-c-9e3b6bbf
type: concept
title: Raise an `HTTPException` in your code[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#raise-an-httpexception-in-your-code
  "Permanent link")
description: '`HTTPException` is a normal Python exception with additional data relevant
  for APIs.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/handling-errors/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Raise an `HTTPException` in your code[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#raise-an-httpexception-in-your-code "Permanent link")

`HTTPException` is a normal Python exception with additional data relevant for APIs.

Because it's a Python exception, you don't `return` it, you `raise` it.

This also means that if you are inside a utility function that you are calling inside of your *path operation function*, and you raise the `HTTPException` from inside of that utility function, it won't run the rest of the code in the *path operation function*, it will terminate that request right away and send the HTTP error from the `HTTPException` to the client.

The benefit of raising an exception over returning a value will be more evident in the section about Dependencies and Security.

In this example, when the client requests an item by an ID that doesn't exist, raise an exception with a status code of `404`:

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