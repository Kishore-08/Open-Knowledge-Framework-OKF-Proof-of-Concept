---
id: fastapi-simple-usage-https-fastapi-tiangolo-com-tutorial-dependencie-5ffb54cb
type: concept
title: Simple usage[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#simple-usage
  "Permanent link")
description: If you look at it, *path operation functions* are declared to be used
  whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling
  the function with the correct parameters, ex
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Simple usage[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#simple-usage "Permanent link")

If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request.

Actually, all (or most) of the web frameworks work in this same way.

You never call those functions directly. They are called by your framework (in this case, **FastAPI**).

With the Dependency Injection system, you can also tell **FastAPI** that your *path operation function* also "depends" on something else that should be executed before your *path operation function*, and **FastAPI** will take care of executing it and "injecting" the results.

Other common terms for this same idea of "dependency injection" are:

- resources
- providers
- services
- injectables
- components