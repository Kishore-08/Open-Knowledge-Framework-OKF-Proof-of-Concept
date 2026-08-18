---
id: fastapi-partial-updates-recap-https-fastapi-tiangolo-com-tutorial-bo-2d06f4f5
type: concept
title: Partial updates recap[¶](https://fastapi.tiangolo.com/tutorial/body-updates/#partial-updates-recap
  "Permanent link")
description: 'In summary, to apply partial updates you would:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-updates/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Partial updates recap[¶](https://fastapi.tiangolo.com/tutorial/body-updates/#partial-updates-recap "Permanent link")

In summary, to apply partial updates you would:

- (Optionally) use `PATCH` instead of `PUT`.
- Retrieve the stored data.
- Put that data in a Pydantic model.
- Generate a `dict` without default values from the input model (using `exclude_unset`).
  - This way you can update only the values actually set by the user, instead of overriding values already stored with default values in your model.
- Create a copy of the stored model, updating its attributes with the received partial updates (using the `update` parameter).
- Convert the copied model to something that can be stored in your DB (for example, using the `jsonable_encoder`).
  - This is comparable to using the model's `.model_dump()` method again, but it makes sure (and converts) the values to data types that can be converted to JSON, for example, `datetime` to `str`.
- Save the data to your DB.
- Return the updated model.

Python 3.10+

```
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}")
async def update_item(item_id: str, item: Item) -> Item:
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.model_dump(exclude_unset=True)
    updated_item = stored_item_model.model_copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
```

Tip

You can actually use this same technique with an HTTP `PUT` operation.

But the example here uses `PATCH` because it was created for these use cases.

Note

Notice that the input model is still validated.

So, if you want to receive partial updates that can omit all the attributes, you need to have a model with all the attributes marked as optional (with default values or `None`).

To distinguish from the models with all optional values for **updates** and models with required values for **creation**, you can use the ideas described in [Extra Models](https://fastapi.tiangolo.com/tutorial/extra-models/).