---
id: fastapi-union-in-python-3-10-https-fastapi-tiangolo-com-tutorial-ext-bcff185a
type: concept
title: '`Union` in Python 3.10[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#union-in-python-3-10
  "Permanent link")'
description: In this example we pass `Union[PlaneItem, CarItem]` as the value of the
  argument `response_model`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/extra-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### `Union` in Python 3.10[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#union-in-python-3-10 "Permanent link")

In this example we pass `Union[PlaneItem, CarItem]` as the value of the argument `response_model`.

Because we are passing it as a **value to an argument** instead of putting it in a **type annotation**, we have to use `Union` even in Python 3.10.

If it was in a type annotation we could have used the vertical bar, as:

```
some_variable: PlaneItem | CarItem
```

But if we put that in the assignment `response_model=PlaneItem | CarItem` we would get an error, because Python would try to perform an **invalid operation** between `PlaneItem` and `CarItem` instead of interpreting that as a type annotation.