---
id: fastapi-run-it-https-fastapi-tiangolo-com-tutorial-security-first-st-3368d50f
type: concept
title: Run it[¶](https://fastapi.tiangolo.com/tutorial/security/first-steps/#run-it
  "Permanent link")
description: Note
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/first-steps/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Run it[¶](https://fastapi.tiangolo.com/tutorial/security/first-steps/#run-it "Permanent link")

Note

The [`python-multipart`](https://github.com/Kludex/python-multipart) package is automatically installed with **FastAPI** when you run the `uv add "fastapi[standard]"` command.

However, if you use the `uv add fastapi` command, the `python-multipart` package is not included by default.

To install it manually, add it to your project with:

```
$ uv add python-multipart
```

This is because **OAuth2** uses "form data" for sending the `username` and `password`.

Run the example with:

```
$ uv run fastapi dev

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```