---
id: fastapi-declare-cookie-parameters-https-fastapi-tiangolo-com-tutoria-6018d1dd
type: concept
title: Declare `Cookie` parameters[¶](https://fastapi.tiangolo.com/tutorial/cookie-params/#declare-cookie-parameters
  "Permanent link")
description: Then declare the cookie parameters using the same structure as with `Path`
  and `Query`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cookie-params/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Declare `Cookie` parameters[¶](https://fastapi.tiangolo.com/tutorial/cookie-params/#declare-cookie-parameters "Permanent link")

Then declare the cookie parameters using the same structure as with `Path` and `Query`.

You can define the default value as well as all the extra validation or annotation parameters:

Python 3.10+

```
from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
```

Technical Details

`Cookie` is a "sister" class of `Path` and `Query`. It also inherits from the same common `Param` class.

But remember that when you import `Query`, `Path`, `Cookie` and others from `fastapi`, those are actually functions that return special classes.

Note

To declare cookies, you need to use `Cookie`, because otherwise the parameters would be interpreted as query parameters.

Note

Have in mind that, as **browsers handle cookies** in special ways and behind the scenes, they **don't** easily allow **JavaScript** to touch them.

If you go to the **API docs UI** at `/docs` you will be able to see the **documentation** for cookies for your *path operations*.

But even if you **fill the data** and click "Execute", because the docs UI works with **JavaScript**, the cookies won't be sent, and you will see an **error** message as if you didn't write any values.

## Recap[¶](https://fastapi.tiangolo.com/tutorial/cookie-params/#recap "Permanent link")

Declare cookies with `Cookie`, using the same common pattern as `Query` and `Path`.