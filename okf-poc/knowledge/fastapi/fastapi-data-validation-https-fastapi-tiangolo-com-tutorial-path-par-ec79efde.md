---
id: fastapi-data-validation-https-fastapi-tiangolo-com-tutorial-path-par-ec79efde
type: concept
title: Data validation[¶](https://fastapi.tiangolo.com/tutorial/path-params/#data-validation
  "Permanent link")
description: 'But if you go to the browser at <http://127.0.0.1:8000/items/foo>, you
  will see a nice HTTP error of:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Data validation[¶](https://fastapi.tiangolo.com/tutorial/path-params/#data-validation "Permanent link")

But if you go to the browser at <http://127.0.0.1:8000/items/foo>, you will see a nice HTTP error of:

```
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "item_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "foo"
    }
  ]
}
```

because the path parameter `item_id` had a value of `"foo"`, which is not an `int`.

The same error would appear if you provided a `float` instead of an `int`, as in: <http://127.0.0.1:8000/items/4.2>

Tip

So, with the same Python type declaration, **FastAPI** gives you data validation.

Notice that the error also clearly states exactly the point where the validation didn't pass.

This is incredibly helpful while developing and debugging code that interacts with your API.