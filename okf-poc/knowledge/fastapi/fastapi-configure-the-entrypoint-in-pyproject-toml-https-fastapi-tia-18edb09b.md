---
id: fastapi-configure-the-entrypoint-in-pyproject-toml-https-fastapi-tia-18edb09b
type: concept
title: Configure the `entrypoint` in `pyproject.toml`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#configure-the-entrypoint-in-pyproject-toml
  "Permanent link")
description: 'As your FastAPI `app` object lives in `app/main.py`, you can configure
  the `entrypoint` in your `pyproject.toml` file like this:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Configure the `entrypoint` in `pyproject.toml`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#configure-the-entrypoint-in-pyproject-toml "Permanent link")

As your FastAPI `app` object lives in `app/main.py`, you can configure the `entrypoint` in your `pyproject.toml` file like this:

```
[tool.fastapi]
entrypoint = "app.main:app"
```

that is equivalent to importing like:

```
from app.main import app
```

That way the `fastapi` command will know where to find your app.

Note

You could also pass the path to the command, like:

```
$ uv run fastapi dev app/main.py
```

But you would have to remember to pass the correct path every time you call the `fastapi` command.

Additionally, other tools might not be able to find it, for example the [VS Code Extension](https://fastapi.tiangolo.com/editor-support/) or [FastAPI Cloud](https://fastapicloud.com), so it is recommended to use the `entrypoint` in `pyproject.toml`.