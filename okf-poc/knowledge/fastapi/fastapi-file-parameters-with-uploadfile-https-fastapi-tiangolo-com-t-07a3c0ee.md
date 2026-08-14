---
id: fastapi-file-parameters-with-uploadfile-https-fastapi-tiangolo-com-t-07a3c0ee
type: concept
title: File Parameters with `UploadFile`[¶](https://fastapi.tiangolo.com/tutorial/request-files/#file-parameters-with-uploadfile
  "Permanent link")
description: 'Define a file parameter with a type of `UploadFile`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## File Parameters with `UploadFile`[¶](https://fastapi.tiangolo.com/tutorial/request-files/#file-parameters-with-uploadfile "Permanent link")

Define a file parameter with a type of `UploadFile`:

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

Using `UploadFile` has several advantages over `bytes`:

- You don't have to use `File()` in the default value of the parameter.
- It uses a "spooled" file:
  - A file stored in memory up to a maximum size limit, and after passing this limit it will be stored on disk.
- This means that it will work well for large files like images, videos, large binaries, etc. without consuming all the memory.
- You can get metadata from the uploaded file.
- It has a [file-like](https://docs.python.org/3/glossary.html#term-file-like-object) `async` interface.
- It exposes an actual Python [`SpooledTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.SpooledTemporaryFile) object that you can pass directly to other libraries that expect a file-like object.