---
id: fastapi-using-the-same-dependency-multiple-times-https-fastapi-tiang-7c664f58
type: concept
title: Using the same dependency multiple times[¶](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#using-the-same-dependency-multiple-times
  "Permanent link")
description: If one of your dependencies is declared multiple times for the same *path
  operation*, for example, multiple dependencies have a common sub-dependency, **FastAPI**
  will know to call that sub-dependency
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Using the same dependency multiple times[¶](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#using-the-same-dependency-multiple-times "Permanent link")

If one of your dependencies is declared multiple times for the same *path operation*, for example, multiple dependencies have a common sub-dependency, **FastAPI** will know to call that sub-dependency only once per request.

And it will save the returned value in a "cache" and pass it to all the "dependants" that need it in that specific request, instead of calling the dependency multiple times for the same request.

In an advanced scenario where you know you need the dependency to be called at every step (possibly multiple times) in the same request instead of using the "cached" value, you can set the parameter `use_cache=False` when using `Depends`:

Python 3.10+Python 3.10+ non-Annotated

```
async def needy_dependency(fresh_value: Annotated[str, Depends(get_value, use_cache=False)]):
    return {"fresh_value": fresh_value}
```

Tip

Prefer to use the `Annotated` version if possible.

```
async def needy_dependency(fresh_value: str = Depends(get_value, use_cache=False)):
    return {"fresh_value": fresh_value}
```