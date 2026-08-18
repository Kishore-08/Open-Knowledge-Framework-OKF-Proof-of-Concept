---
id: fastapi-declare-a-path-parameter-https-fastapi-tiangolo-com-tutorial-ec79efde
type: concept
title: Declare a *path parameter*[¶](https://fastapi.tiangolo.com/tutorial/path-params/#declare-a-path-parameter
  "Permanent link")
description: 'Then create a *path parameter* with a type annotation using the enum
  class you created (`ModelName`):'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Declare a *path parameter*[¶](https://fastapi.tiangolo.com/tutorial/path-params/#declare-a-path-parameter "Permanent link")

Then create a *path parameter* with a type annotation using the enum class you created (`ModelName`):

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