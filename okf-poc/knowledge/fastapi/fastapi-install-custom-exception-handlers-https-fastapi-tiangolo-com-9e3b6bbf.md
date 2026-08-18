---
id: fastapi-install-custom-exception-handlers-https-fastapi-tiangolo-com-9e3b6bbf
type: concept
title: Install custom exception handlers[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers
  "Permanent link")
description: You can add custom exception handlers with [the same exception utilities
  from Starlette](https://starlette.dev/exceptions/).
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/handling-errors/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Install custom exception handlers[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers "Permanent link")

You can add custom exception handlers with [the same exception utilities from Starlette](https://starlette.dev/exceptions/).

Let's say you have a custom exception `UnicornException` that you (or a library you use) might `raise`.

And you want to handle this exception globally with FastAPI.

You could add a custom exception handler with `@app.exception_handler()`:

Python 3.10+

```
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
```

Here, if you request `/unicorns/yolo`, the *path operation* will `raise` a `UnicornException`.

But it will be handled by the `unicorn_exception_handler`.

So, you will receive a clean error, with an HTTP status code of `418` and a JSON content of:

```
{"message": "Oops! yolo did something. There goes a rainbow..."}
```

Technical Details

You could also use `from starlette.requests import Request` and `from starlette.responses import JSONResponse`.

**FastAPI** provides the same `starlette.responses` as `fastapi.responses` just as a convenience for you, the developer. But most of the available responses come directly from Starlette. The same with `Request`.