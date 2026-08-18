---
id: fastapi-other-models-https-fastapi-tiangolo-com-tutorial-security-ge-6666a3a6
type: concept
title: Other models[¶](https://fastapi.tiangolo.com/tutorial/security/get-current-user/#other-models
  "Permanent link")
description: You can now get the current user directly in the *path operation functions*
  and deal with the security mechanisms at the **Dependency Injection** level, using
  `Depends`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/get-current-user/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Other models[¶](https://fastapi.tiangolo.com/tutorial/security/get-current-user/#other-models "Permanent link")

You can now get the current user directly in the *path operation functions* and deal with the security mechanisms at the **Dependency Injection** level, using `Depends`.

And you can use any model or data for the security requirements (in this case, a Pydantic model `User`).

But you are not restricted to using some specific data model, class or type.

Do you want to have an `id` and `email` and not have any `username` in your model? Sure. You can use these same tools.

Do you want to just have a `str`? Or just a `dict`? Or a database class model instance directly? It all works the same way.

You actually don't have users that log in to your application but robots, bots, or other systems, that have just an access token? Again, it all works the same.

Just use any kind of model, any kind of class, any kind of database that you need for your application. **FastAPI** has you covered with the dependency injection system.