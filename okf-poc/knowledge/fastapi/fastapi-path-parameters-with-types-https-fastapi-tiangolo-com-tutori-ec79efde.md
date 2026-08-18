---
id: fastapi-path-parameters-with-types-https-fastapi-tiangolo-com-tutori-ec79efde
type: concept
title: Path parameters with types[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters-with-types
  "Permanent link")
description: 'You can declare the type of a path parameter in the function, using
  standard Python type annotations:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Path parameters with types[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters-with-types "Permanent link")

You can declare the type of a path parameter in the function, using standard Python type annotations:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

In this case, `item_id` is declared to be an `int`.

Tip

This will give you editor support inside of your function, with error checks, completion, etc.