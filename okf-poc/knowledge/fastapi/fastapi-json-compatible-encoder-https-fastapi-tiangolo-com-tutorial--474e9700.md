---
id: fastapi-json-compatible-encoder-https-fastapi-tiangolo-com-tutorial--474e9700
type: concept
title: JSON Compatible Encoder[¶](https://fastapi.tiangolo.com/tutorial/encoder/#json-c
description: There are some cases where you might need to convert a data type (like
  a Pydantic model) to something compatible with JSON (like a `dict`, `list`, etc).
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/encoder/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# JSON Compatible Encoder[¶](https://fastapi.tiangolo.com/tutorial/encoder/#json-compatible-encoder "Permanent link")

There are some cases where you might need to convert a data type (like a Pydantic model) to something compatible with JSON (like a `dict`, `list`, etc).

For example, if you need to store it in a database.

For that, **FastAPI** provides a `jsonable_encoder()` function.