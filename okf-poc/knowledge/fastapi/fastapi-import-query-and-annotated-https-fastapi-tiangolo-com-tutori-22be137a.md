---
id: fastapi-import-query-and-annotated-https-fastapi-tiangolo-com-tutori-22be137a
type: concept
title: Import `Query` and `Annotated`[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#import-query-and-annotated
  "Permanent link")
description: 'To achieve that, first import:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Import `Query` and `Annotated`[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#import-query-and-annotated "Permanent link")

To achieve that, first import:

- `Query` from `fastapi`
- `Annotated` from `typing`

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

Note

FastAPI added support for `Annotated` (and started recommending it) in version 0.95.0.

If you have an older version, you would get errors when trying to use `Annotated`.

Make sure you [Upgrade the FastAPI version](https://fastapi.tiangolo.com/deployment/versions/#upgrading-the-fastapi-versions) to at least 0.95.1 before using `Annotated`.