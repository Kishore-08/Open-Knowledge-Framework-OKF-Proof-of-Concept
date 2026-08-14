---
id: fastapi-cors-preflight-requests-https-fastapi-tiangolo-com-tutorial--4f1cea92
type: concept
title: CORS preflight requests[¶](https://fastapi.tiangolo.com/tutorial/cors/#cors-preflight-requests
  "Permanent link")
description: These are any `OPTIONS` request with `Origin` and `Access-Control-Request-Method`
  headers.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cors/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### CORS preflight requests[¶](https://fastapi.tiangolo.com/tutorial/cors/#cors-preflight-requests "Permanent link")

These are any `OPTIONS` request with `Origin` and `Access-Control-Request-Method` headers.

In this case the middleware will intercept the incoming request and respond with appropriate CORS headers, and either a `200` or `400` response for informational purposes.