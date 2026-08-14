---
id: fastapi-reuse-fastapi-s-exception-handlers-https-fastapi-tiangolo-co-9e3b6bbf
type: concept
title: Reuse **FastAPI**'s exception handlers[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#reuse-fastapis-exception-handlers
  "Permanent link")
description: 'If you want to use the exception along with the same default exception
  handlers from **FastAPI**, you can import and reuse the default exception handlers
  from `fastapi.exception_handlers`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/handling-errors/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Reuse **FastAPI**'s exception handlers[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#reuse-fastapis-exception-handlers "Permanent link")

If you want to use the exception along with the same default exception handlers from **FastAPI**, you can import and reuse the default exception handlers from `fastapi.exception_handlers`:

Python 3.10+

```
from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}
```

In this example you are just printing the error with a very expressive message, but you get the idea. You can use the exception and then just reuse the default exception handlers.