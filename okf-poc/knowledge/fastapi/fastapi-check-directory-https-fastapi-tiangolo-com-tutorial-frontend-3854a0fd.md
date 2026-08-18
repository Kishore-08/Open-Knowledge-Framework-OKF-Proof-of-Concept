---
id: fastapi-check-directory-https-fastapi-tiangolo-com-tutorial-frontend-3854a0fd
type: concept
title: Check Directory[¶](https://fastapi.tiangolo.com/tutorial/frontend/#check-directory
  "Permanent link")
description: By default, `app.frontend()` uses `check_dir="auto"`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/frontend/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Check Directory[¶](https://fastapi.tiangolo.com/tutorial/frontend/#check-directory "Permanent link")

By default, `app.frontend()` uses `check_dir="auto"`.

When the `FASTAPI_ENV` environment variable is set to `development`, **FastAPI** only shows a warning if the frontend build output directory is missing. The [`fastapi dev` command](https://github.com/fastapi/fastapi-cli#fastapi-dev) sets this environment variable for you if it is not already set. This lets you start the backend before building or starting the frontend during development.

In any other environment, **FastAPI** raises an error when the app is created. This helps catch configuration errors early before deploying an app without its frontend files.

You can also set `check_dir=True` to always check the directory when the app is created.

If your frontend files are created later, for example by a separate build step after the app object is created, set `check_dir=False`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

app.frontend("/", directory="dist", check_dir=False)
```

With `check_dir=False`, **FastAPI** will not check the directory when the app is created. If the configured directory is still missing when a request is handled, **FastAPI** will raise an error then.