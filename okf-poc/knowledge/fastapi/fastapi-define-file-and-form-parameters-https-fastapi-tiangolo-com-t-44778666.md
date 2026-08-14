---
id: fastapi-define-file-and-form-parameters-https-fastapi-tiangolo-com-t-44778666
type: concept
title: Define `File` and `Form` parameters[¶](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/#define-file-and-form-parameters
  "Permanent link")
description: 'Create file and form parameters the same way you would for `Body` or
  `Query`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-forms-and-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Define `File` and `Form` parameters[¶](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/#define-file-and-form-parameters "Permanent link")

Create file and form parameters the same way you would for `Body` or `Query`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
```

The files and form fields will be uploaded as form data and you will receive the files and form fields.

And you can declare some of the files as `bytes` and some as `UploadFile`.

Warning

You can declare multiple `File` and `Form` parameters in a *path operation*, but you can't also declare `Body` fields that you expect to receive as JSON, as the request will have the body encoded using `multipart/form-data` instead of `application/json`.

This is not a limitation of **FastAPI**, it's part of the HTTP protocol.

## Recap[¶](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/#recap "Permanent link")

Use `File` and `Form` together when you need to receive data and files in the same request.