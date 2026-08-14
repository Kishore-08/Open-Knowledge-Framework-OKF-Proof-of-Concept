---
id: fastapi-custom-validation-https-fastapi-tiangolo-com-tutorial-query--22be137a
type: concept
title: Custom Validation[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#custom-validation
  "Permanent link")
description: There could be cases where you need to do some **custom validation**
  that can't be done with the parameters shown above.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Custom Validation[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#custom-validation "Permanent link")

There could be cases where you need to do some **custom validation** that can't be done with the parameters shown above.

In those cases, you can use a **custom validator function** that is applied after the normal validation (e.g. after validating that the value is a `str`).

You can achieve that using [Pydantic's `AfterValidator`](https://pydantic.dev/docs/validation/latest/concepts/validators/#field-after-validator) inside of `Annotated`.

Tip

Pydantic also has [`BeforeValidator`](https://pydantic.dev/docs/validation/latest/concepts/validators/#field-before-validator) and others. 🤓

For example, this custom validator checks that the item ID starts with `isbn-` for an ISBN book number or with `imdb-` for an IMDB movie URL ID:

Python 3.10+

```
import random
from typing import Annotated

from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
```

Note

This is available with Pydantic version 2 or above. 😎

Tip

If you need to do any type of validation that requires communicating with any **external component**, like a database or another API, you should instead use **FastAPI Dependencies**, you will learn about them later.

These custom validators are for things that can be checked with **only** the **same data** provided in the request.