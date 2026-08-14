---
id: fastapi-uploadfile-with-additional-metadata-https-fastapi-tiangolo-c-07a3c0ee
type: concept
title: '`UploadFile` with Additional Metadata[¶](https://fastapi.tiangolo.com/tutorial/request-files/#uploadfile-with-additional-metadata
  "Permanent link")'
description: 'You can also use `File()` with `UploadFile`, for example, to set additional
  metadata:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## `UploadFile` with Additional Metadata[¶](https://fastapi.tiangolo.com/tutorial/request-files/#uploadfile-with-additional-metadata "Permanent link")

You can also use `File()` with `UploadFile`, for example, to set additional metadata:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(description="A file read as bytes")):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile = File(description="A file read as UploadFile"),
):
    return {"filename": file.filename}
```