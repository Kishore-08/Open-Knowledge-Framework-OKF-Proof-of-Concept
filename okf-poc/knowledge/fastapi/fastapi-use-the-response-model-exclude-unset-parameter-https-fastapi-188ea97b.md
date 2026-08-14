---
id: fastapi-use-the-response-model-exclude-unset-parameter-https-fastapi-188ea97b
type: concept
title: Use the `response_model_exclude_unset` parameter[¶](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response-model-exclude-unset-parameter
  "Permanent link")
description: 'You can set the *path operation decorator* parameter `response_model_exclude_unset=True`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Use the `response_model_exclude_unset` parameter[¶](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response-model-exclude-unset-parameter "Permanent link")

You can set the *path operation decorator* parameter `response_model_exclude_unset=True`:

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
```

and those default values won't be included in the response, only the values actually set.

So, if you send a request to that *path operation* for the item with ID `foo`, the response (not including default values) will be:

```
{
    "name": "Foo",
    "price": 50.2
}
```

Note

You can also use:

- `response_model_exclude_defaults=True`
- `response_model_exclude_none=True`

as described in [the Pydantic docs](https://pydantic.dev/docs/validation/latest/concepts/serialization/#excluding-and-including-fields-based-on-their-value) for `exclude_defaults` and `exclude_none`.

#### Data with values for fields with defaults[¶](https://fastapi.tiangolo.com/tutorial/response-model/#data-with-values-for-fields-with-defaults "Permanent link")

But if your data has values for the model's fields with default values, like the item with ID `bar`:

```
{
    "name": "Bar",
    "description": "The bartenders",
    "price": 62,
    "tax": 20.2
}
```

they will be included in the response.

#### Data with the same values as the defaults[¶](https://fastapi.tiangolo.com/tutorial/response-model/#data-with-the-same-values-as-the-defaults "Permanent link")

If the data has the same values as the default ones, like the item with ID `baz`:

```
{
    "name": "Baz",
    "description": None,
    "price": 50.2,
    "tax": 10.5,
    "tags": []
}
```

FastAPI is smart enough (actually, Pydantic is smart enough) to realize that, even though `description`, `tax`, and `tags` have the same values as the defaults, they were set explicitly (instead of taken from the defaults).

So, they will be included in the JSON response.

Tip

Notice that the default values can be anything, not only `None`.

They can be a list (`[]`), a `float` of `10.5`, etc.