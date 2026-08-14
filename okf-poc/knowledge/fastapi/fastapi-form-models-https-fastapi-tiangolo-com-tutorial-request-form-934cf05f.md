---
id: fastapi-form-models-https-fastapi-tiangolo-com-tutorial-request-form-934cf05f
type: concept
title: Form Models[¶](https://fastapi.tiangolo.com/tutorial/request-form-models/#form-m
description: You can use **Pydantic models** to declare **form fields** in FastAPI.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-form-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Form Models[¶](https://fastapi.tiangolo.com/tutorial/request-form-models/#form-models "Permanent link")

You can use **Pydantic models** to declare **form fields** in FastAPI.

Note

To use forms, first install [`python-multipart`](https://github.com/Kludex/python-multipart).

Add it to your project:

```
$ uv add python-multipart
```

Note

This is supported since FastAPI version `0.113.0`. 🤓