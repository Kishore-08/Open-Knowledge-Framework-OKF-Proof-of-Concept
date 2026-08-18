---
id: fastapi-recap-https-fastapi-tiangolo-com-tutorial-query-params-str-v-22be137a
type: concept
title: Recap[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#recap
  "Permanent link")
description: You can declare additional validations and metadata for your parameters.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Recap[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#recap "Permanent link")

You can declare additional validations and metadata for your parameters.

Generic validations and metadata:

- `alias`
- `title`
- `description`
- `deprecated`

Validations specific for strings:

- `min_length`
- `max_length`
- `pattern`

Custom validations using `AfterValidator`.

In these examples you saw how to declare validations for `str` values.

See the next chapters to learn how to declare validations for other types, like numbers.