---
id: fastapi-response-status-code-https-fastapi-tiangolo-com-tutorial-res-0daf007f
type: concept
title: Response Status Code[¶](https://fastapi.tiangolo.com/tutorial/response-status-co
description: 'The same way you can specify a response model, you can also declare
  the HTTP status code used for the response with the parameter `status_code` in any
  of the *path operations*:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-status-code/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Response Status Code[¶](https://fastapi.tiangolo.com/tutorial/response-status-code/#response-status-code "Permanent link")

The same way you can specify a response model, you can also declare the HTTP status code used for the response with the parameter `status_code` in any of the *path operations*:

- `@app.get()`
- `@app.post()`
- `@app.put()`
- `@app.delete()`
- etc.

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
```

Note

Notice that `status_code` is a parameter of the "decorator" method (`get`, `post`, etc). Not of your *path operation function*, like all the parameters and body.

The `status_code` parameter receives a number with the HTTP status code.

Note

`status_code` can alternatively also receive an `IntEnum`, such as Python's [`http.HTTPStatus`](https://docs.python.org/3/library/http.html#http.HTTPStatus).

It will:

- Return that status code in the response.
- Document it as such in the OpenAPI schema (and so, in the user interfaces):

Note

Some response codes (see the next section) indicate that the response does not have a body.

FastAPI knows this, and will produce OpenAPI docs that state there is no response body.