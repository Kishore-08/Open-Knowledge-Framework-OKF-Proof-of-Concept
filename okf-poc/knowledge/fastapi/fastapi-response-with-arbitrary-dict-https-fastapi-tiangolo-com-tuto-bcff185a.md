---
id: fastapi-response-with-arbitrary-dict-https-fastapi-tiangolo-com-tuto-bcff185a
type: concept
title: Response with arbitrary `dict`[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#response-with-arbitrary-dict
  "Permanent link")
description: You can also declare a response using a plain arbitrary `dict`, declaring
  just the type of the keys and values, without using a Pydantic model.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/extra-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Response with arbitrary `dict`[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#response-with-arbitrary-dict "Permanent link")

You can also declare a response using a plain arbitrary `dict`, declaring just the type of the keys and values, without using a Pydantic model.

This is useful if you don't know the valid field/attribute names (that would be needed for a Pydantic model) beforehand.

In this case, you can use `dict`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/keyword-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}
```