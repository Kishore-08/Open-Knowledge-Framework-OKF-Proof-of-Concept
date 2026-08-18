---
id: fastapi-using-context-managers-in-dependencies-with-yield-https-fast-5c0232ed
type: concept
title: Using context managers in dependencies with `yield`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#using-context-managers-in-dependencies-with-yield
  "Permanent link")
description: Warning
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Using context managers in dependencies with `yield`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#using-context-managers-in-dependencies-with-yield "Permanent link")

Warning

This is, more or less, an "advanced" idea.

If you are just starting with **FastAPI** you might want to skip it for now.

In Python, you can create Context Managers by [creating a class with two methods: `__enter__()` and `__exit__()`](https://docs.python.org/3/reference/datamodel.html#context-managers).

You can also use them inside of **FastAPI** dependencies with `yield` by using
`with` or `async with` statements inside of the dependency function:

Python 3.10+

```
class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    with MySuperContextManager() as db:
        yield db
```

Tip

Another way to create a context manager is with:

- [`@contextlib.contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) or
- [`@contextlib.asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager)

using them to decorate a function with a single `yield`.

That's what **FastAPI** uses internally for dependencies with `yield`.

But you don't have to use the decorators for FastAPI dependencies (and you shouldn't).

FastAPI will do it for you internally.