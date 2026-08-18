---
id: fastapi-bodies-of-arbitrary-dict-s-https-fastapi-tiangolo-com-tutori-99d5900d
type: concept
title: Bodies of arbitrary `dict`s[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#bodies-of-arbitrary-dicts
  "Permanent link")
description: You can also declare a body as a `dict` with keys of some type and values
  of some other type.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Bodies of arbitrary `dict`s[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#bodies-of-arbitrary-dicts "Permanent link")

You can also declare a body as a `dict` with keys of some type and values of some other type.

This way, you don't have to know beforehand what the valid field/attribute names are (as would be the case with Pydantic models).

This would be useful if you want to receive keys that you don't already know.

---

Another useful case is when you want to have keys of another type (e.g., `int`).

That's what we are going to see here.

In this case, you would accept any `dict` as long as it has `int` keys with `float` values:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
```

Tip

Keep in mind that JSON only supports `str` as keys.

But Pydantic has automatic data conversion.

This means that, even though your API clients can only send strings as keys, as long as those strings contain pure integers, Pydantic will convert them and validate them.

And the `dict` you receive as `weights` will actually have `int` keys and `float` values.