---
id: fastapi-warning-about-replacing-https-fastapi-tiangolo-com-tutorial--2d06f4f5
type: concept
title: Warning about replacing[¶](https://fastapi.tiangolo.com/tutorial/body-updates/#warning-about-replacing
  "Permanent link")
description: 'That means that if you want to update the item `bar` using `PUT` with
  a body containing:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-updates/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Warning about replacing[¶](https://fastapi.tiangolo.com/tutorial/body-updates/#warning-about-replacing "Permanent link")

That means that if you want to update the item `bar` using `PUT` with a body containing:

```
{
    "name": "Barz",
    "price": 3,
    "description": None,
}
```

because it doesn't include the already stored attribute `"tax": 20.2`, the input model would take the default value of `"tax": 10.5`.

And the data would be saved with that "new" `tax` of `10.5`.