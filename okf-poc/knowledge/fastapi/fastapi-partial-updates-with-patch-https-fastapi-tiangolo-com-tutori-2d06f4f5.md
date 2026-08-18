---
id: fastapi-partial-updates-with-patch-https-fastapi-tiangolo-com-tutori-2d06f4f5
type: concept
title: Partial updates with `PATCH`[¶](https://fastapi.tiangolo.com/tutorial/body-updates/#partial-updates-with-patch
  "Permanent link")
description: You can also use the [HTTP `PATCH`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH)
  operation to *partially* update data.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-updates/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Partial updates with `PATCH`[¶](https://fastapi.tiangolo.com/tutorial/body-updates/#partial-updates-with-patch "Permanent link")

You can also use the [HTTP `PATCH`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH) operation to *partially* update data.

This means that you can send only the data that you want to update, leaving the rest intact.

Note

`PATCH` is less commonly used and known than `PUT`.

And many teams use only `PUT`, even for partial updates.

You are **free** to use them however you want, **FastAPI** doesn't impose any restrictions.

But this guide shows you, more or less, how they are intended to be used.