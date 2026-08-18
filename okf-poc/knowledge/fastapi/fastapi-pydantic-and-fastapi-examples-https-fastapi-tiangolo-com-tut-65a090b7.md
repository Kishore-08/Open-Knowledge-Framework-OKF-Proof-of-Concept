---
id: fastapi-pydantic-and-fastapi-examples-https-fastapi-tiangolo-com-tut-65a090b7
type: concept
title: Pydantic and FastAPI `examples`[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#pydantic-and-fastapi-examples
  "Permanent link")
description: When you add `examples` inside a Pydantic model, using `schema_extra`
  or `Field(examples=["something"])` that example is added to the **JSON Schema**
  for that Pydantic model.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Pydantic and FastAPI `examples`[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#pydantic-and-fastapi-examples "Permanent link")

When you add `examples` inside a Pydantic model, using `schema_extra` or `Field(examples=["something"])` that example is added to the **JSON Schema** for that Pydantic model.

And that **JSON Schema** of the Pydantic model is included in the **OpenAPI** of your API, and then it's used in the docs UI.

In versions of FastAPI before 0.99.0 (0.99.0 and above use the newer OpenAPI 3.1.0) when you used `example` or `examples` with any of the other utilities (`Query()`, `Body()`, etc.) those examples were not added to the JSON Schema that describes that data (not even to OpenAPI's own version of JSON Schema), they were added directly to the *path operation* declaration in OpenAPI (outside the parts of OpenAPI that use JSON Schema).

But now that FastAPI 0.99.0 and above uses OpenAPI 3.1.0, that uses JSON Schema 2020-12, and Swagger UI 5.0.0 and above, everything is more consistent and the examples are included in JSON Schema.