---
id: fastapi-path-convertor-https-fastapi-tiangolo-com-tutorial-path-para-ec79efde
type: concept
title: Path convertor[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-convertor
  "Permanent link")
description: 'Using an option directly from Starlette you can declare a *path parameter*
  containing a *path* using a URL like:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Path convertor[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-convertor "Permanent link")

Using an option directly from Starlette you can declare a *path parameter* containing a *path* using a URL like:

```
/files/{file_path:path}
```

In this case, the name of the parameter is `file_path`, and the last part, `:path`, tells it that the parameter should match any *path*.

So, you can use it with:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

Tip

You might need the parameter to contain `/home/johndoe/myfile.txt`, with a leading slash (`/`).

In that case, the URL would be: `/files//home/johndoe/myfile.txt`, with a double slash (`//`) between `files` and `home`.