---
id: fastapi-form-data-https-fastapi-tiangolo-com-tutorial-request-forms--16928256
type: concept
title: Form Data[¶](https://fastapi.tiangolo.com/tutorial/request-forms/#form-data
  "Per
description: When you need to receive form fields instead of JSON, you can use `Form`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-forms/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Form Data[¶](https://fastapi.tiangolo.com/tutorial/request-forms/#form-data "Permanent link")

When you need to receive form fields instead of JSON, you can use `Form`.

Note

To use forms, first install [`python-multipart`](https://github.com/Kludex/python-multipart).

Add it to your project:

```
$ uv add python-multipart
```