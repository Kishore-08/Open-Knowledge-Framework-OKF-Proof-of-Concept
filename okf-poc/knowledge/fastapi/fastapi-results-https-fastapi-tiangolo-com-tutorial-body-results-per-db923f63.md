---
id: fastapi-results-https-fastapi-tiangolo-com-tutorial-body-results-per-db923f63
type: concept
title: Results[¶](https://fastapi.tiangolo.com/tutorial/body/#results "Permanent link")
description: 'With just that Python type declaration, **FastAPI** will:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Results[¶](https://fastapi.tiangolo.com/tutorial/body/#results "Permanent link")

With just that Python type declaration, **FastAPI** will:

- Read the body of the request as JSON.
- Convert the corresponding types (if needed).
- Validate the data.
  - If the data is invalid, it will return a nice and clear error, indicating exactly where and what was the incorrect data.
- Give you the received data in the parameter `item`.
  - As you declared it in the function to be of type `Item`, you will also have all the editor support (completion, etc) for all of the attributes and their types.
- Generate [JSON Schema](https://json-schema.org) definitions for your model, you can also use them anywhere else you like if it makes sense for your project.
- Those schemas will be part of the generated OpenAPI schema, and used by the automatic documentation UIs.