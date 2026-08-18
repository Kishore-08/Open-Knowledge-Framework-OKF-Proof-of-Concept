---
id: fastapi-dependencies-with-yield-https-fastapi-tiangolo-com-tutorial--5c0232ed
type: concept
title: Dependencies with yield[¶](https://fastapi.tiangolo.com/tutorial/dependencies/de
description: FastAPI supports dependencies that do some extra steps after finishing.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Dependencies with yield[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield "Permanent link")

FastAPI supports dependencies that do some extra steps after finishing.

To do this, use `yield` instead of `return`, and write the extra steps (code) after.

Tip

Make sure to use `yield` one single time per dependency.

Technical Details

Any function that is valid to use with:

- [`@contextlib.contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) or
- [`@contextlib.asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager)

would be valid to use as a **FastAPI** dependency.

In fact, FastAPI uses those two decorators internally.