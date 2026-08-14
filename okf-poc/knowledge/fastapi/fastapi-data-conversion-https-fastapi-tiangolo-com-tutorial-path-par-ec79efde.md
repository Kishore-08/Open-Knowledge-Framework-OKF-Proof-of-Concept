---
id: fastapi-data-conversion-https-fastapi-tiangolo-com-tutorial-path-par-ec79efde
type: concept
title: Data conversion[¶](https://fastapi.tiangolo.com/tutorial/path-params/#data-conversion
  "Permanent link")
description: 'If you run this example and open your browser at <http://127.0.0.1:8000/items/3>,
  you will see a response of:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Data conversion[¶](https://fastapi.tiangolo.com/tutorial/path-params/#data-conversion "Permanent link")

If you run this example and open your browser at <http://127.0.0.1:8000/items/3>, you will see a response of:

```
{"item_id":3}
```

Tip

Notice that the value your function received (and returned) is `3`, as a Python `int`, not a string `"3"`.

So, with that type declaration, **FastAPI** gives you automatic request "parsing".