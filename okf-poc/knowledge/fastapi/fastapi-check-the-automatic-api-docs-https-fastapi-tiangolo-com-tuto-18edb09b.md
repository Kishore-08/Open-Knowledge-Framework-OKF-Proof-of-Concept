---
id: fastapi-check-the-automatic-api-docs-https-fastapi-tiangolo-com-tuto-18edb09b
type: concept
title: Check the automatic API docs[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#check-the-automatic-api-docs
  "Permanent link")
description: 'Now, run your app:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Check the automatic API docs[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#check-the-automatic-api-docs "Permanent link")

Now, run your app:

```
$ uv run fastapi dev

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

And open the docs at <http://127.0.0.1:8000/docs>.

You will see the automatic API docs, including the paths from all the submodules, using the correct paths (and prefixes) and the correct tags: