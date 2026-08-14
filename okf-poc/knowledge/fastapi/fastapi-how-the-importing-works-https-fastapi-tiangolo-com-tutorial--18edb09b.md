---
id: fastapi-how-the-importing-works-https-fastapi-tiangolo-com-tutorial--18edb09b
type: concept
title: How the importing works[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#how-the-importing-works
  "Permanent link")
description: 'The section:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### How the importing works[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#how-the-importing-works "Permanent link")

The section:

```
from .routers import items, users
```

means:

- Starting in the same package that this module (the file `app/main.py`) lives in (the directory `app/`)...
- look for the subpackage `routers` (the directory at `app/routers/`)...
- and from it, import the submodule `items` (the file at `app/routers/items.py`) and `users` (the file at `app/routers/users.py`)...

The module `items` will have a variable `router` (`items.router`). This is the same one we created in the file `app/routers/items.py`, it's an `APIRouter` object.

And then we do the same for the module `users`.

We could also import them like:

```
from app.routers import items, users
```

Note

The first version is a "relative import":

```
from .routers import items, users
```

The second version is an "absolute import":

```
from app.routers import items, users
```

To learn more about Python Packages and Modules, read [the official Python documentation about Modules](https://docs.python.org/3/tutorial/modules.html).