---
id: fastapi-fastapi-data-filtering-https-fastapi-tiangolo-com-tutorial-r-188ea97b
type: concept
title: FastAPI Data Filtering[¶](https://fastapi.tiangolo.com/tutorial/response-model/#fastapi-data-filtering
  "Permanent link")
description: Now, for FastAPI, it will see the return type and make sure that what
  you return includes **only** the fields that are declared in the type.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### FastAPI Data Filtering[¶](https://fastapi.tiangolo.com/tutorial/response-model/#fastapi-data-filtering "Permanent link")

Now, for FastAPI, it will see the return type and make sure that what you return includes **only** the fields that are declared in the type.

FastAPI does several things internally with Pydantic to make sure that those same rules of class inheritance are not used for the returned data filtering, otherwise you could end up returning much more data than what you expected.

This way, you can get the best of both worlds: type annotations with **tooling support** and **data filtering**.