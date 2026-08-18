---
id: fastapi-examples-in-json-schema-openapi-https-fastapi-tiangolo-com-t-65a090b7
type: concept
title: '`examples` in JSON Schema - OpenAPI[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#examples-in-json-schema-openapi
  "Permanent link")'
description: 'When using any of:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## `examples` in JSON Schema - OpenAPI[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#examples-in-json-schema-openapi "Permanent link")

When using any of:

- `Path()`
- `Query()`
- `Header()`
- `Cookie()`
- `Body()`
- `Form()`
- `File()`

you can also declare a group of `examples` with additional information that will be added to their **JSON Schemas** inside of **OpenAPI**.