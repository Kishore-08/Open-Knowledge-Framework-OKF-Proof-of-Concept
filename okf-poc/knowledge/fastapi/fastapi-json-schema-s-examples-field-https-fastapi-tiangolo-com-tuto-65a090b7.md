---
id: fastapi-json-schema-s-examples-field-https-fastapi-tiangolo-com-tuto-65a090b7
type: concept
title: JSON Schema's `examples` field[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#json-schemas-examples-field
  "Permanent link")
description: But then JSON Schema added an [`examples`](https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.9.5)
  field to a new version of the specification.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### JSON Schema's `examples` field[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#json-schemas-examples-field "Permanent link")

But then JSON Schema added an [`examples`](https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.9.5) field to a new version of the specification.

And then the new OpenAPI 3.1.0 was based on the latest version (JSON Schema 2020-12) that included this new field `examples`.

And now this new `examples` field takes precedence over the old single (and custom) `example` field, that is now deprecated.

This new `examples` field in JSON Schema is **just a `list`** of examples, not a dict with extra metadata as in the other places in OpenAPI (described above).

Note

Even after OpenAPI 3.1.0 was released with this new simpler integration with JSON Schema, for a while, Swagger UI, the tool that provides the automatic docs, didn't support OpenAPI 3.1.0 (it does since version 5.0.0 🎉).

Because of that, versions of FastAPI previous to 0.99.0 still used versions of OpenAPI lower than 3.1.0.