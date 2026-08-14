---
id: fastapi-import-file-and-form-https-fastapi-tiangolo-com-tutorial-req-44778666
type: concept
title: Import `File` and `Form`[¶](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/#import-file-and-form
  "Permanent link")
description: Python 3.10+
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-forms-and-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Import `File` and `Form`[¶](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/#import-file-and-form "Permanent link")

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