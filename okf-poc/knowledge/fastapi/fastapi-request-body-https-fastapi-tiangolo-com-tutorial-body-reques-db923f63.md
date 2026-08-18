---
id: fastapi-request-body-https-fastapi-tiangolo-com-tutorial-body-reques-db923f63
type: concept
title: Request Body[¶](https://fastapi.tiangolo.com/tutorial/body/#request-body "Perman
description: When you need to send data from a client (let's say, a browser) to your
  API, you send it as a **request body**.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Request Body[¶](https://fastapi.tiangolo.com/tutorial/body/#request-body "Permanent link")

When you need to send data from a client (let's say, a browser) to your API, you send it as a **request body**.

A **request** body is data sent by the client to your API. A **response** body is the data your API sends to the client.

Your API almost always has to send a **response** body. But clients don't necessarily need to send **request bodies** all the time, sometimes they only request a path, maybe with some query parameters, but don't send a body.

To declare a **request** body, you use [Pydantic](https://pydantic.dev/docs/) models with all their power and benefits.

Note

To send data, you should use one of: `POST` (the most common), `PUT`, `DELETE` or `PATCH`.

Sending a body with a `GET` request has an undefined behavior in the specifications, nevertheless, it is supported by FastAPI, only for very complex/extreme use cases.

As it is discouraged, the interactive docs with Swagger UI won't show the documentation for the body when using `GET`, and proxies in the middle might not support it.