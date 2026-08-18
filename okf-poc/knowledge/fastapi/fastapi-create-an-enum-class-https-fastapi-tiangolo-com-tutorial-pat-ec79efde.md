---
id: fastapi-create-an-enum-class-https-fastapi-tiangolo-com-tutorial-pat-ec79efde
type: concept
title: Create an `Enum` class[¶](https://fastapi.tiangolo.com/tutorial/path-params/#create-an-enum-class
  "Permanent link")
description: Import `Enum` and create a sub-class that inherits from `str` and from
  `Enum`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Create an `Enum` class[¶](https://fastapi.tiangolo.com/tutorial/path-params/#create-an-enum-class "Permanent link")

Import `Enum` and create a sub-class that inherits from `str` and from `Enum`.

By inheriting from `str` the API docs will be able to know that the values must be of type `string` and will be able to render correctly.

Then create class attributes with fixed values, which will be the available valid values:

Python 3.10+

```
from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

Tip

If you are wondering, "AlexNet", "ResNet", and "LeNet" are just names of Machine Learning models.