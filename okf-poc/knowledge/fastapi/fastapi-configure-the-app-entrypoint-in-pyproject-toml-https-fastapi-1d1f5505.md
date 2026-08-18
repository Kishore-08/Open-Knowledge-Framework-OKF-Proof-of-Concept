---
id: fastapi-configure-the-app-entrypoint-in-pyproject-toml-https-fastapi-1d1f5505
type: concept
title: Configure the app `entrypoint` in `pyproject.toml`[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#configure-the-app-entrypoint-in-pyproject-toml
  "Permanent link")
description: 'You can configure where your app is located in a `pyproject.toml` file
  like:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/first-steps/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Configure the app `entrypoint` in `pyproject.toml`[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#configure-the-app-entrypoint-in-pyproject-toml "Permanent link")

You can configure where your app is located in a `pyproject.toml` file like:

```
[tool.fastapi]
entrypoint = "main:app"
```

That `entrypoint` will tell the `fastapi` command that it should import the app like:

```
from main import app
```

If your code was structured like:

```
.
├── backend
│   ├── main.py
│   ├── __init__.py
```

Then you would set the `entrypoint` as:

```
[tool.fastapi]
entrypoint = "backend.main:app"
```

which would be equivalent to:

```
from backend.main import app
```