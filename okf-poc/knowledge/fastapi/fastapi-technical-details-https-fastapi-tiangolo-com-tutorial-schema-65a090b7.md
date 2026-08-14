---
id: fastapi-technical-details-https-fastapi-tiangolo-com-tutorial-schema-65a090b7
type: concept
title: Technical Details[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#technical-details
  "Permanent link")
description: Tip
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Technical Details[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#technical-details "Permanent link")

Tip

If you are already using **FastAPI** version **0.99.0 or above**, you can probably **skip** these details.

They are more relevant for older versions, before OpenAPI 3.1.0 was available.

You can consider this a brief OpenAPI and JSON Schema **history lesson**. 🤓

Warning

These are very technical details about the standards **JSON Schema** and **OpenAPI**.

If the ideas above already work for you, that might be enough, and you probably don't need these details, feel free to skip them.

Before OpenAPI 3.1.0, OpenAPI used an older and modified version of **JSON Schema**.

JSON Schema didn't have `examples`, so OpenAPI added its own `example` field to its own modified version.

OpenAPI also added `example` and `examples` fields to other parts of the specification:

- [`Parameter Object` (in the specification)](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#parameter-object) that was used by FastAPI's:
  - `Path()`
  - `Query()`
  - `Header()`
  - `Cookie()`
- [`Request Body Object`, in the field `content`, on the `Media Type Object` (in the specification)](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#media-type-object) that was used by FastAPI's:
  - `Body()`
  - `File()`
  - `Form()`

Note

This old OpenAPI-specific `examples` parameter is now `openapi_examples` since FastAPI `0.103.0`.