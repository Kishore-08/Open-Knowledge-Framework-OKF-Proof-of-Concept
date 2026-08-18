---
id: fastapi-working-with-python-enumerations-https-fastapi-tiangolo-com--ec79efde
type: concept
title: Working with Python *enumerations*[¶](https://fastapi.tiangolo.com/tutorial/path-params/#working-with-python-enumerations
  "Permanent link")
description: The value of the *path parameter* will be an *enumeration member*.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Working with Python *enumerations*[¶](https://fastapi.tiangolo.com/tutorial/path-params/#working-with-python-enumerations "Permanent link")

The value of the *path parameter* will be an *enumeration member*.

#### Compare *enumeration members*[¶](https://fastapi.tiangolo.com/tutorial/path-params/#compare-enumeration-members "Permanent link")

You can compare it with the *enumeration member* in your created enum `ModelName`:

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

#### Get the *enumeration value*[¶](https://fastapi.tiangolo.com/tutorial/path-params/#get-the-enumeration-value "Permanent link")

You can get the actual value (a `str` in this case) using `model_name.value`, or in general, `your_enum_member.value`:

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

You could also access the value `"lenet"` with `ModelName.lenet.value`.

#### Return *enumeration members*[¶](https://fastapi.tiangolo.com/tutorial/path-params/#return-enumeration-members "Permanent link")

You can return *enum members* from your *path operation*, even nested in a JSON body (e.g. a `dict`).

They will be converted to their corresponding values (strings in this case) before returning them to the client:

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

In your client you will get a JSON response like:

```
{
  "model_name": "alexnet",
  "message": "Deep Learning FTW!"
}
```