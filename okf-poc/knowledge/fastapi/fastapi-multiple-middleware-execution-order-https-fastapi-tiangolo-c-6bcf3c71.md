---
id: fastapi-multiple-middleware-execution-order-https-fastapi-tiangolo-c-6bcf3c71
type: concept
title: Multiple middleware execution order[¶](https://fastapi.tiangolo.com/tutorial/middleware/#multiple-middleware-execution-order
  "Permanent link")
description: 'When you add multiple middlewares using either `@app.middleware()` decorator
  or `app.add_middleware()` method, each new middleware wraps the application, forming
  a stack. The last middleware added is '
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/middleware/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Multiple middleware execution order[¶](https://fastapi.tiangolo.com/tutorial/middleware/#multiple-middleware-execution-order "Permanent link")

When you add multiple middlewares using either `@app.middleware()` decorator or `app.add_middleware()` method, each new middleware wraps the application, forming a stack. The last middleware added is the *outermost*, and the first is the *innermost*.

On the request path, the *outermost* middleware runs first.

On the response path, it runs last.

For example:

```
app.add_middleware(MiddlewareA)
app.add_middleware(MiddlewareB)
```

This results in the following execution order:

- **Request**: MiddlewareB → MiddlewareA → route
- **Response**: route → MiddlewareA → MiddlewareB

This stacking behavior ensures that middlewares are executed in a predictable and controllable order.