---
id: fastapi-override-the-default-exception-handlers-https-fastapi-tiango-9e3b6bbf
type: concept
title: Override the default exception handlers[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#override-the-default-exception-handlers
  "Permanent link")
description: '**FastAPI** has some default exception handlers.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/handling-errors/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Override the default exception handlers[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#override-the-default-exception-handlers "Permanent link")

**FastAPI** has some default exception handlers.

These handlers are in charge of returning the default JSON responses when you `raise` an `HTTPException` and when the request has invalid data.

You can override these exception handlers with your own.