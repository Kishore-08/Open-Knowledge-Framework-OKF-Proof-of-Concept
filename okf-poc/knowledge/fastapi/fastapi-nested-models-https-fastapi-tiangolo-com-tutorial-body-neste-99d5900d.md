---
id: fastapi-nested-models-https-fastapi-tiangolo-com-tutorial-body-neste-99d5900d
type: concept
title: Nested Models[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#nested-models
  "Permanent link")
description: Each attribute of a Pydantic model has a type.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Nested Models[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#nested-models "Permanent link")

Each attribute of a Pydantic model has a type.

But that type can itself be another Pydantic model.

So, you can declare deeply nested JSON "objects" with specific attribute names, types and validations.

All that, arbitrarily nested.