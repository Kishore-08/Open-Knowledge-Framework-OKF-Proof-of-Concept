---
id: fastapi-header-parameter-models-https-fastapi-tiangolo-com-tutorial--22664928
type: concept
title: Header Parameter Models[¶](https://fastapi.tiangolo.com/tutorial/header-param-mo
description: If you have a group of related **header parameters**, you can create
  a **Pydantic model** to declare them.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/header-param-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Header Parameter Models[¶](https://fastapi.tiangolo.com/tutorial/header-param-models/#header-parameter-models "Permanent link")

If you have a group of related **header parameters**, you can create a **Pydantic model** to declare them.

This would allow you to **re-use the model** in **multiple places** and also to declare validations and metadata for all the parameters at once. 😎

Note

This is supported since FastAPI version `0.115.0`. 🤓