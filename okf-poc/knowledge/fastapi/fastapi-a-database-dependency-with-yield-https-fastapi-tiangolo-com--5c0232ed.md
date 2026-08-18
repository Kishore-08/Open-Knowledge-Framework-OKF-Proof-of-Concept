---
id: fastapi-a-database-dependency-with-yield-https-fastapi-tiangolo-com--5c0232ed
type: concept
title: A database dependency with `yield`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-database-dependency-with-yield
  "Permanent link")
description: For example, you could use this to create a database session and close
  it after finishing.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## A database dependency with `yield`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-database-dependency-with-yield "Permanent link")

For example, you could use this to create a database session and close it after finishing.

Only the code prior to and including the `yield` statement is executed before creating a response:

Python 3.10+

```
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

The yielded value is what is injected into *path operations* and other dependencies:

Python 3.10+

```
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

The code following the `yield` statement is executed after the response:

Python 3.10+

```
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

Tip

You can use `async` or regular functions.

**FastAPI** will do the right thing with each, the same as with normal dependencies.