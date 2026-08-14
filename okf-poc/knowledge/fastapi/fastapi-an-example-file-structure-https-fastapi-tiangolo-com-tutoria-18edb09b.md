---
id: fastapi-an-example-file-structure-https-fastapi-tiangolo-com-tutoria-18edb09b
type: concept
title: An example file structure[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure
  "Permanent link")
description: 'Let''s say you have a file structure like this:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## An example file structure[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure "Permanent link")

Let's say you have a file structure like this:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

Tip

There are several `__init__.py` files: one in each directory or subdirectory.

This is what allows importing code from one file into another.

For example, in `app/main.py` you could have a line like:

```
from app.routers import items
```

- The `app` directory contains everything. And it has an empty file `app/__init__.py`, so it is a "Python package" (a collection of "Python modules"): `app`.
- It contains an `app/main.py` file. As it is inside a Python package (a directory with a file `__init__.py`), it is a "module" of that package: `app.main`.
- There's also an `app/dependencies.py` file, just like `app/main.py`, it is a "module": `app.dependencies`.
- There's a subdirectory `app/routers/` with another file `__init__.py`, so it's a "Python subpackage": `app.routers`.
- The file `app/routers/items.py` is inside a package, `app/routers/`, so, it's a submodule: `app.routers.items`.
- The same with `app/routers/users.py`, it's another submodule: `app.routers.users`.
- There's also a subdirectory `app/internal/` with another file `__init__.py`, so it's another "Python subpackage": `app.internal`.
- And the file `app/internal/admin.py` is another submodule: `app.internal.admin`.

The same file structure with comments:

```
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin
```