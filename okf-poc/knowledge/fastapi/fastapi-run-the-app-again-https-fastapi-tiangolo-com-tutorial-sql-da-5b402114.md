---
id: fastapi-run-the-app-again-https-fastapi-tiangolo-com-tutorial-sql-da-5b402114
type: concept
title: Run the App Again[¶](https://fastapi.tiangolo.com/tutorial/sql-databases/#run-the-app-again
  "Permanent link")
description: 'You can run the app again:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/sql-databases/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Run the App Again[¶](https://fastapi.tiangolo.com/tutorial/sql-databases/#run-the-app-again "Permanent link")

You can run the app again:

```
$ uv run fastapi dev

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

If you go to the `/docs` API UI, you will see that it is now updated, and it won't expect to receive the `id` from the client when creating a hero, etc.