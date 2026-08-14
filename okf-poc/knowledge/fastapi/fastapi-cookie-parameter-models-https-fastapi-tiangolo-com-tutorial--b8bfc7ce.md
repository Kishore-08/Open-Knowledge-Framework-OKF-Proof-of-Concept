---
id: fastapi-cookie-parameter-models-https-fastapi-tiangolo-com-tutorial--b8bfc7ce
type: concept
title: Cookie Parameter Models[¶](https://fastapi.tiangolo.com/tutorial/cookie-param-mo
description: If you have a group of **cookies** that are related, you can create a
  **Pydantic model** to declare them. 🍪
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cookie-param-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Cookie Parameter Models[¶](https://fastapi.tiangolo.com/tutorial/cookie-param-models/#cookie-parameter-models "Permanent link")

If you have a group of **cookies** that are related, you can create a **Pydantic model** to declare them. 🍪

This would allow you to **re-use the model** in **multiple places** and also to declare validations and metadata for all the parameters at once. 😎

Note

This is supported since FastAPI version `0.115.0`. 🤓

Tip

This same technique applies to `Query`, `Cookie`, and `Header`. 😎