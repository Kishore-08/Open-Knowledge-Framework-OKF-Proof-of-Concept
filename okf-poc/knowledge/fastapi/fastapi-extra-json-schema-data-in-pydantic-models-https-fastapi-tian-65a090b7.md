---
id: fastapi-extra-json-schema-data-in-pydantic-models-https-fastapi-tian-65a090b7
type: concept
title: Extra JSON Schema data in Pydantic models[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#extra-json-schema-data-in-pydantic-models
  "Permanent link")
description: You can declare `examples` for a Pydantic model that will be added to
  the generated JSON Schema.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Extra JSON Schema data in Pydantic models[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#extra-json-schema-data-in-pydantic-models "Permanent link")

You can declare `examples` for a Pydantic model that will be added to the generated JSON Schema.

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

That extra info will be added as-is to the output **JSON Schema** for that model, and it will be used in the API docs.

You can use the attribute `model_config` that takes a `dict` as described in [Pydantic's docs: Configuration](https://pydantic.dev/docs/validation/latest/api/pydantic/config/).

You can set `"json_schema_extra"` with a `dict` containing any additional data you would like to show up in the generated JSON Schema, including `examples`.

Tip

You could use the same technique to extend the JSON Schema and add your own custom extra info.

For example you could use it to add metadata for a frontend user interface, etc.

Note

OpenAPI 3.1.0 (used since FastAPI 0.99.0) added support for `examples`, which is part of the **JSON Schema** standard.

Before that, it only supported the keyword `example` with a single example. That is still supported by OpenAPI 3.1.0, but is deprecated and is not part of the JSON Schema standard. So you are encouraged to migrate `example` to `examples`. 🤓

You can read more at the end of this page.