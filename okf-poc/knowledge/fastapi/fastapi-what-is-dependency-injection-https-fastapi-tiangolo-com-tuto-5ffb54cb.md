---
id: fastapi-what-is-dependency-injection-https-fastapi-tiangolo-com-tuto-5ffb54cb
type: concept
title: What is "Dependency Injection"[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#what-is-dependency-injection
  "Permanent link")
description: '**"Dependency Injection"** means, in programming, that there is a way
  for your code (in this case, your *path operation functions*) to declare things
  that it requires to work and use: "dependencies".'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## What is "Dependency Injection"[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#what-is-dependency-injection "Permanent link")

**"Dependency Injection"** means, in programming, that there is a way for your code (in this case, your *path operation functions*) to declare things that it requires to work and use: "dependencies".

And then, that system (in this case **FastAPI**) will take care of doing whatever is needed to provide your code with those needed dependencies ("inject" the dependencies).

This is very useful when you need to:

- Have shared logic (the same code logic again and again).
- Share database connections.
- Enforce security, authentication, role requirements, etc.
- And many other things...

All these, while minimizing code repetition.