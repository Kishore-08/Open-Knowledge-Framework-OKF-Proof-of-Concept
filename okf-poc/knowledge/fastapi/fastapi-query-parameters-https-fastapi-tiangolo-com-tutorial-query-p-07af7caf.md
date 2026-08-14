---
id: fastapi-query-parameters-https-fastapi-tiangolo-com-tutorial-query-p-07af7caf
type: concept
title: Query Parameters[¶](https://fastapi.tiangolo.com/tutorial/query-params/#query-pa
description: When you declare other function parameters that are not part of the path
  parameters, they are automatically interpreted as "query" parameters.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Query Parameters[¶](https://fastapi.tiangolo.com/tutorial/query-params/#query-parameters "Permanent link")

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

The query is the set of key-value pairs that go after the `?` in a URL, separated by `&` characters.

For example, in the URL:

```
http://127.0.0.1:8000/items/?skip=0&limit=10
```

...the query parameters are:

- `skip`: with a value of `0`
- `limit`: with a value of `10`

As they are part of the URL, they are "naturally" strings.

But when you declare them with Python types (in the example above, as `int`), they are converted to that type and validated against it.

All the same processes that apply to path parameters also apply to query parameters:

- Editor support (obviously)
- Data "parsing"
- Data validation
- Automatic documentation