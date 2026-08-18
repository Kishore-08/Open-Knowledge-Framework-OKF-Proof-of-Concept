---
id: fastapi-multiple-file-uploads-with-additional-metadata-https-fastapi-07a3c0ee
type: concept
title: Multiple File Uploads with Additional Metadata[¶](https://fastapi.tiangolo.com/tutorial/request-files/#multiple-file-uploads-with-additional-metadata
  "Permanent link")
description: 'And the same way as before, you can use `File()` to set additional parameters,
  even for `UploadFile`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-files/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Multiple File Uploads with Additional Metadata[¶](https://fastapi.tiangolo.com/tutorial/request-files/#multiple-file-uploads-with-additional-metadata "Permanent link")

And the same way as before, you can use `File()` to set additional parameters, even for `UploadFile`:

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(
    files: list[bytes] = File(description="Multiple files as bytes"),
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: list[UploadFile] = File(description="Multiple files as UploadFile"),
):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
```

## Recap[¶](https://fastapi.tiangolo.com/tutorial/request-files/#recap "Permanent link")

Use `File`, `bytes`, and `UploadFile` to declare files to be uploaded in the request, sent as form data.