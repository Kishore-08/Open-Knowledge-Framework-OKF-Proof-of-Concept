---
id: fastapi-bodies-of-pure-lists-https-fastapi-tiangolo-com-tutorial-bod-99d5900d
type: concept
title: Bodies of pure lists[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#bodies-of-pure-lists
  "Permanent link")
description: 'If the top level value of the JSON body you expect is a JSON `array`
  (a Python `list`), you can declare the type in the parameter of the function, the
  same as in Pydantic models:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Bodies of pure lists[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#bodies-of-pure-lists "Permanent link")

If the top level value of the JSON body you expect is a JSON `array` (a Python `list`), you can declare the type in the parameter of the function, the same as in Pydantic models:

```
images: list[Image]
```

as in:

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images
```