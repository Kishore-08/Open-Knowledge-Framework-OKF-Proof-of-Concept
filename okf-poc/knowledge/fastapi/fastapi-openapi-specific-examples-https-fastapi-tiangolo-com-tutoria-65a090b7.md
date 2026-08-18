---
id: fastapi-openapi-specific-examples-https-fastapi-tiangolo-com-tutoria-65a090b7
type: concept
title: OpenAPI-specific `examples`[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#openapi-specific-examples
  "Permanent link")
description: Since before **JSON Schema** supported `examples`, OpenAPI had support
  for a different field also called `examples`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### OpenAPI-specific `examples`[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#openapi-specific-examples "Permanent link")

Since before **JSON Schema** supported `examples`, OpenAPI had support for a different field also called `examples`.

This **OpenAPI-specific** `examples` goes in another section in the OpenAPI specification. It goes in the **details for each *path operation***, not inside each JSON Schema.

And Swagger UI has supported this particular `examples` field for a while. So, you can use it to **show** different **examples in the docs UI**.

The shape of this OpenAPI-specific field `examples` is a `dict` with **multiple examples** (instead of a `list`), each with extra information that will be added to **OpenAPI** too.

This doesn't go inside of each JSON Schema contained in OpenAPI, this goes outside, in the *path operation* directly.