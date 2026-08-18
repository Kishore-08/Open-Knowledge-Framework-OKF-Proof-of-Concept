---
id: fastapi-dependencies-in-path-operation-decorators-https-fastapi-tian-9cbf10cd
type: concept
title: Dependencies in path operation decorators[¶](https://fastapi.tiangolo.com/tutori
description: In some cases you don't really need the return value of a dependency
  inside your *path operation function*.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Dependencies in path operation decorators[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/#dependencies-in-path-operation-decorators "Permanent link")

In some cases you don't really need the return value of a dependency inside your *path operation function*.

Or the dependency doesn't return a value.

But you still need it to be executed/solved.

For those cases, instead of declaring a *path operation function* parameter with `Depends`, you can add a `list` of `dependencies` to the *path operation decorator*.