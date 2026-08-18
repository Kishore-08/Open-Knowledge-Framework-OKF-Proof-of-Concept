---
id: fastapi-more-info-https-fastapi-tiangolo-com-tutorial-cors-more-info-4f1cea92
type: concept
title: More info[¶](https://fastapi.tiangolo.com/tutorial/cors/#more-info "Permanent
  link")
description: For more info about CORS, check the [Mozilla CORS documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cors/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## More info[¶](https://fastapi.tiangolo.com/tutorial/cors/#more-info "Permanent link")

For more info about CORS, check the [Mozilla CORS documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

Technical Details

You could also use `from starlette.middleware.cors import CORSMiddleware`.

**FastAPI** provides several middlewares in `fastapi.middleware` just as a convenience for you, the developer. But most of the available middlewares come directly from Starlette.