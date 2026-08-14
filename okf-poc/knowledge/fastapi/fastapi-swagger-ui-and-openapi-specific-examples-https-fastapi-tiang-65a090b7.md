---
id: fastapi-swagger-ui-and-openapi-specific-examples-https-fastapi-tiang-65a090b7
type: concept
title: Swagger UI and OpenAPI-specific `examples`[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#swagger-ui-and-openapi-specific-examples
  "Permanent link")
description: Now, as Swagger UI didn't support multiple JSON Schema examples (as of
  2023-08-26), users didn't have a way to show multiple examples in the docs.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Swagger UI and OpenAPI-specific `examples`[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#swagger-ui-and-openapi-specific-examples "Permanent link")

Now, as Swagger UI didn't support multiple JSON Schema examples (as of 2023-08-26), users didn't have a way to show multiple examples in the docs.

To solve that, FastAPI `0.103.0` **added support** for declaring the same old **OpenAPI-specific** `examples` field with the new parameter `openapi_examples`. 🤓