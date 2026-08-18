---
id: fastapi-defaults-https-fastapi-tiangolo-com-tutorial-query-params-de-07af7caf
type: concept
title: Defaults[¶](https://fastapi.tiangolo.com/tutorial/query-params/#defaults "Permanent
  link")
description: As query parameters are not a fixed part of a path, they can be optional
  and can have default values.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Defaults[¶](https://fastapi.tiangolo.com/tutorial/query-params/#defaults "Permanent link")

As query parameters are not a fixed part of a path, they can be optional and can have default values.

In the example above they have default values of `skip=0` and `limit=10`.

So, going to the URL:

```
http://127.0.0.1:8000/items/
```

would be the same as going to:

```
http://127.0.0.1:8000/items/?skip=0&limit=10
```

But if you go to, for example:

```
http://127.0.0.1:8000/items/?skip=20
```

The parameter values in your function will be:

- `skip=20`: because you set it in the URL
- `limit=10`: because that was the default value