---
id: fastapi-optional-file-upload-https-fastapi-tiangolo-com-tutorial-req-07a3c0ee
type: concept
title: Optional File Upload[¶](https://fastapi.tiangolo.com/tutorial/request-files/#optional-file-upload
  "Permanent link")
description: 'You can make a file optional by using standard type annotations and
  setting a default value of `None`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Optional File Upload[¶](https://fastapi.tiangolo.com/tutorial/request-files/#optional-file-upload "Permanent link")

You can make a file optional by using standard type annotations and setting a default value of `None`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
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
async def create_file(file: bytes | None = File(default=None)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}
```