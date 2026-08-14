---
id: fastapi-request-files-https-fastapi-tiangolo-com-tutorial-request-fi-07a3c0ee
type: concept
title: Request Files[¶](https://fastapi.tiangolo.com/tutorial/request-files/#request-fi
description: You can define files to be uploaded by the client using `File`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Request Files[¶](https://fastapi.tiangolo.com/tutorial/request-files/#request-files "Permanent link")

You can define files to be uploaded by the client using `File`.

Note

To receive uploaded files, first install [`python-multipart`](https://github.com/Kludex/python-multipart).

Add it to your project:

```
$ uv add python-multipart
```

This is because uploaded files are sent as "form data".