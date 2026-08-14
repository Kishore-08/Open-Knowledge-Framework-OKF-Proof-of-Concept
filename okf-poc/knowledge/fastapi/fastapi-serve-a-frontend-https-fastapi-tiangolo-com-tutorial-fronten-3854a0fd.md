---
id: fastapi-serve-a-frontend-https-fastapi-tiangolo-com-tutorial-fronten-3854a0fd
type: concept
title: Serve a Frontend[¶](https://fastapi.tiangolo.com/tutorial/frontend/#serve-a-frontend
  "Permanent link")
description: After building your frontend, for example with `npm run build`, put the
  generated files in a directory, for example, `dist`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/frontend/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Serve a Frontend[¶](https://fastapi.tiangolo.com/tutorial/frontend/#serve-a-frontend "Permanent link")

After building your frontend, for example with `npm run build`, put the generated files in a directory, for example, `dist`.

Your project structure could look like this:

```
.
├── pyproject.toml
├── app
│   ├── __init__.py
│   └── main.py
└── dist
    ├── index.html
    └── assets
        └── app.js
```

Then serve it with `app.frontend()`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

app.frontend("/", directory="dist")
```

With this, a request for `/assets/app.js` can serve `dist/assets/app.js`.

If you also have a **FastAPI** *path operation*, the *path operation* wins.