---
id: fastapi-invalid-return-type-annotations-https-fastapi-tiangolo-com-t-188ea97b
type: concept
title: Invalid Return Type Annotations[¶](https://fastapi.tiangolo.com/tutorial/response-model/#invalid-return-type-annotations
  "Permanent link")
description: But when you return some other arbitrary object that is not a valid Pydantic
  type (e.g. a database object) and you annotate it like that in the function, FastAPI
  will try to create a Pydantic response
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Invalid Return Type Annotations[¶](https://fastapi.tiangolo.com/tutorial/response-model/#invalid-return-type-annotations "Permanent link")

But when you return some other arbitrary object that is not a valid Pydantic type (e.g. a database object) and you annotate it like that in the function, FastAPI will try to create a Pydantic response model from that type annotation, and will fail.

The same would happen if you had something like a union between different types where one or more of them are not valid Pydantic types, for example this would fail 💥:

Python 3.10+

```
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}
```

...this fails because the type annotation is not a Pydantic type and is not just a single `Response` class or subclass, it's a union (any of the two) between a `Response` and a `dict`.