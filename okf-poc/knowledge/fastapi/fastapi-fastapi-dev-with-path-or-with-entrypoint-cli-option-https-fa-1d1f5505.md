---
id: fastapi-fastapi-dev-with-path-or-with-entrypoint-cli-option-https-fa-1d1f5505
type: concept
title: '`fastapi dev` with path or with `--entrypoint` CLI option[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#fastapi-dev-with-path-or-with-entrypoint-cli-option
  "Permanent link")'
description: 'You can also pass the file path to the `fastapi dev` command, and it
  will guess the FastAPI app object to use:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/first-steps/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### `fastapi dev` with path or with `--entrypoint` CLI option[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#fastapi-dev-with-path-or-with-entrypoint-cli-option "Permanent link")

You can also pass the file path to the `fastapi dev` command, and it will guess the FastAPI app object to use:

```
$ uv run fastapi dev main.py
```

Or, you can also pass the `--entrypoint` option to the `fastapi dev` command:

```
$ uv run fastapi dev --entrypoint main:app
```

But you would have to remember to pass the correct path\entrypoint every time you call the `fastapi` command.

Additionally, other tools might not be able to find it, for example the [VS Code Extension](https://fastapi.tiangolo.com/editor-support/) or [FastAPI Cloud](https://fastapicloud.com), so it is recommended to use the `entrypoint` in `pyproject.toml`.