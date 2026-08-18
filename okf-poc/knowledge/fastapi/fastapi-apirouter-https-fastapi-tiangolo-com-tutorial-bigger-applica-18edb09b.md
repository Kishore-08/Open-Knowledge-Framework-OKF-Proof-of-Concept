---
id: fastapi-apirouter-https-fastapi-tiangolo-com-tutorial-bigger-applica-18edb09b
type: concept
title: '`APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter
  "Permanent link")'
description: Let's say the file dedicated to handling just users is the submodule
  at `/app/routers/users.py`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter "Permanent link")

Let's say the file dedicated to handling just users is the submodule at `/app/routers/users.py`.

You want to have the *path operations* related to your users separated from the rest of the code, to keep it organized.

But it's still part of the same **FastAPI** application/web API (it's part of the same "Python Package").

You can create the *path operations* for that module using `APIRouter`.