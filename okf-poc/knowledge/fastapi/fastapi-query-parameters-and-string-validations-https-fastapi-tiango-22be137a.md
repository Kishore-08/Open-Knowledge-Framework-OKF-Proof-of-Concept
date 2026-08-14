---
id: fastapi-query-parameters-and-string-validations-https-fastapi-tiango-22be137a
type: concept
title: Query Parameters and String Validations[¶](https://fastapi.tiangolo.com/tutorial
description: '**FastAPI** allows you to declare additional information and validation
  for your parameters.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Query Parameters and String Validations[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-parameters-and-string-validations "Permanent link")

**FastAPI** allows you to declare additional information and validation for your parameters.

Let's take this application as example:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

The query parameter `q` is of type `str | None`, that means that it's of type `str` but could also be `None`, and indeed, the default value is `None`, so FastAPI will know it's not required.

Note

FastAPI will know that the value of `q` is not required because of the default value `= None`.

Having `str | None` will allow your editor to give you better support and detect errors.