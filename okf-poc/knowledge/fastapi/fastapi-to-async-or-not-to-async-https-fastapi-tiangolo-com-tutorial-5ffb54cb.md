---
id: fastapi-to-async-or-not-to-async-https-fastapi-tiangolo-com-tutorial-5ffb54cb
type: concept
title: To `async` or not to `async`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#to-async-or-not-to-async
  "Permanent link")
description: As dependencies will also be called by **FastAPI** (the same as your
  *path operation functions*), the same rules apply while defining your functions.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## To `async` or not to `async`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#to-async-or-not-to-async "Permanent link")

As dependencies will also be called by **FastAPI** (the same as your *path operation functions*), the same rules apply while defining your functions.

You can use `async def` or normal `def`.

And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, etc.

It doesn't matter. **FastAPI** will know what to do.

Note

If you don't know, check the [Async: *"In a hurry?"*](https://fastapi.tiangolo.com/async/#in-a-hurry) section about `async` and `await` in the docs.