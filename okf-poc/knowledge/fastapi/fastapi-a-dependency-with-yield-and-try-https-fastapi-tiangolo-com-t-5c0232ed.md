---
id: fastapi-a-dependency-with-yield-and-try-https-fastapi-tiangolo-com-t-5c0232ed
type: concept
title: A dependency with `yield` and `try`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-dependency-with-yield-and-try
  "Permanent link")
description: If you use a `try` block in a dependency with `yield`, you'll receive
  any exception that was thrown when using the dependency.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## A dependency with `yield` and `try`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-dependency-with-yield-and-try "Permanent link")

If you use a `try` block in a dependency with `yield`, you'll receive any exception that was thrown when using the dependency.

For example, if some code at some point in the middle, in another dependency or in a *path operation*, made a database transaction "rollback" or created any other exception, you would receive the exception in your dependency.

So, you can look for that specific exception inside the dependency with `except SomeException`.

In the same way, you can use `finally` to make sure the exit steps are executed, no matter if there was an exception or not.

Python 3.10+

```
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```