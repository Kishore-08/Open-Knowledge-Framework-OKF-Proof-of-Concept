---
id: fastapi-query-as-the-default-value-or-in-annotated-https-fastapi-tia-22be137a
type: concept
title: '`Query` as the default value or in `Annotated`[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-as-the-default-value-or-in-annotated
  "Permanent link")'
description: Keep in mind that when using `Query` inside of `Annotated` you cannot
  use the `default` parameter for `Query`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### `Query` as the default value or in `Annotated`[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-as-the-default-value-or-in-annotated "Permanent link")

Keep in mind that when using `Query` inside of `Annotated` you cannot use the `default` parameter for `Query`.

Instead, use the actual default value of the function parameter. Otherwise, it would be inconsistent.

For example, this is not allowed:

```
q: Annotated[str, Query(default="rick")] = "morty"
```

...because it's not clear if the default value should be `"rick"` or `"morty"`.

So, you would use (preferably):

```
q: Annotated[str, Query()] = "rick"
```

...or in older code bases you will find:

```
q: str = Query(default="rick")
```