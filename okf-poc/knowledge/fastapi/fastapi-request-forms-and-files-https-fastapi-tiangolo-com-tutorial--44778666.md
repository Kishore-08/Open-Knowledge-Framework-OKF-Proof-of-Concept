---
id: fastapi-request-forms-and-files-https-fastapi-tiangolo-com-tutorial--44778666
type: concept
title: Request Forms and Files[¶](https://fastapi.tiangolo.com/tutorial/request-forms-a
description: You can define files and form fields at the same time using `File` and
  `Form`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-forms-and-files/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Request Forms and Files[¶](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/#request-forms-and-files "Permanent link")

You can define files and form fields at the same time using `File` and `Form`.

Note

To receive uploaded files and/or form data, first install [`python-multipart`](https://github.com/Kludex/python-multipart).

Add it to your project:

```
$ uv add python-multipart
```