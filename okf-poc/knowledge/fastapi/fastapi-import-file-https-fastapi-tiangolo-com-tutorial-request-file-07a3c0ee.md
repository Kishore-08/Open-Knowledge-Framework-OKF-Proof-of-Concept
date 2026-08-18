---
id: fastapi-import-file-https-fastapi-tiangolo-com-tutorial-request-file-07a3c0ee
type: concept
title: Import `File`[¶](https://fastapi.tiangolo.com/tutorial/request-files/#import-file
  "Permanent link")
description: 'Import `File` and `UploadFile` from `fastapi`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-files/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Import `File`[¶](https://fastapi.tiangolo.com/tutorial/request-files/#import-file "Permanent link")

Import `File` and `UploadFile` from `fastapi`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
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
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
```