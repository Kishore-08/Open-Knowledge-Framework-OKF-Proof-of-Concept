---
id: fastapi-response-model-priority-https-fastapi-tiangolo-com-tutorial--188ea97b
type: concept
title: '`response_model` Priority[¶](https://fastapi.tiangolo.com/tutorial/response-model/#response-model-priority
  "Permanent link")'
description: If you declare both a return type and a `response_model`, the `response_model`
  will take priority and be used by FastAPI.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### `response_model` Priority[¶](https://fastapi.tiangolo.com/tutorial/response-model/#response-model-priority "Permanent link")

If you declare both a return type and a `response_model`, the `response_model` will take priority and be used by FastAPI.

This way you can add correct type annotations to your functions even when you are returning a type different than the response model, to be used by the editor and tools like mypy. And still you can have FastAPI do the data validation, documentation, etc. using the `response_model`.

You can also use `response_model=None` to disable creating a response model for that *path operation*, you might need to do it if you are adding type annotations for things that are not valid Pydantic fields, you will see an example of that in one of the sections below.