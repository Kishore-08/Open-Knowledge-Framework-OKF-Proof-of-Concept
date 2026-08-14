---
id: fastapi-handling-errors-https-fastapi-tiangolo-com-tutorial-handling-9e3b6bbf
type: concept
title: Handling Errors[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#handli
description: There are many situations in which you need to report an error to a client
  that is using your API.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/handling-errors/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Handling Errors[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#handling-errors "Permanent link")

There are many situations in which you need to report an error to a client that is using your API.

This client could be a browser with a frontend, a code from someone else, an IoT device, etc.

You could need to tell the client that:

- The client doesn't have enough privileges for that operation.
- The client doesn't have access to that resource.
- The item the client was trying to access doesn't exist.
- etc.

In these cases, you would normally return an **HTTP status code** in the range of **400** (from 400 to 499).

This is similar to the 200 HTTP status codes (from 200 to 299). Those "200" status codes mean that somehow there was a "success" in the request.

The status codes in the 400 range mean that there was an error from the client.

Remember all those **"404 Not Found"** errors (and jokes)?

## Use `HTTPException`[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#use-httpexception "Permanent link")

To return HTTP responses with errors to the client you use `HTTPException`.