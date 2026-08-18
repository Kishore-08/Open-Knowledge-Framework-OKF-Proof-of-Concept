---
id: fastapi-define-file-parameters-https-fastapi-tiangolo-com-tutorial-r-07a3c0ee
type: concept
title: Define `File` Parameters[¶](https://fastapi.tiangolo.com/tutorial/request-files/#define-file-parameters
  "Permanent link")
description: 'Create file parameters the same way you would for `Body` or `Form`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-files/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Define `File` Parameters[¶](https://fastapi.tiangolo.com/tutorial/request-files/#define-file-parameters "Permanent link")

Create file parameters the same way you would for `Body` or `Form`:

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

Note

`File` is a class that inherits directly from `Form`.

But remember that when you import `Query`, `Path`, `File` and others from `fastapi`, those are actually functions that return special classes.

Tip

To declare File bodies, you need to use `File`, because otherwise the parameters would be interpreted as query parameters or body (JSON) parameters.

The files will be uploaded as "form data".

If you declare the type of your *path operation function* parameter as `bytes`, **FastAPI** will read the file for you and you will receive the contents as `bytes`.

Keep in mind that this means that the whole contents will be stored in memory. This will work well for small files.

But there are several cases in which you might benefit from using `UploadFile`.