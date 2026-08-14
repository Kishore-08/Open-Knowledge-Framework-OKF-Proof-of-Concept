---
id: fastapi-query-parameter-models-https-fastapi-tiangolo-com-tutorial-q-a2cdd64f
type: concept
title: Query Parameter Models[¶](https://fastapi.tiangolo.com/tutorial/query-param-mode
description: If you have a group of **query parameters** that are related, you can
  create a **Pydantic model** to declare them.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-param-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Query Parameter Models[¶](https://fastapi.tiangolo.com/tutorial/query-param-models/#query-parameter-models "Permanent link")

If you have a group of **query parameters** that are related, you can create a **Pydantic model** to declare them.

This would allow you to **re-use the model** in **multiple places** and also to declare validations and metadata for all the parameters at once. 😎

Note

This is supported since FastAPI version `0.115.0`. 🤓