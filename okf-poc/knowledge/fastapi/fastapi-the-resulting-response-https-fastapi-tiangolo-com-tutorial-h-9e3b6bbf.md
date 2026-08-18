---
id: fastapi-the-resulting-response-https-fastapi-tiangolo-com-tutorial-h-9e3b6bbf
type: concept
title: The resulting response[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#the-resulting-response
  "Permanent link")
description: 'If the client requests `http://example.com/items/foo` (an `item_id`
  `"foo"`), that client will receive an HTTP status code of 200, and a JSON response
  of:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/handling-errors/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### The resulting response[¶](https://fastapi.tiangolo.com/tutorial/handling-errors/#the-resulting-response "Permanent link")

If the client requests `http://example.com/items/foo` (an `item_id` `"foo"`), that client will receive an HTTP status code of 200, and a JSON response of:

```
{
  "item": "The Foo Wrestlers"
}
```

But if the client requests `http://example.com/items/bar` (a non-existent `item_id` `"bar"`), that client will receive an HTTP status code of 404 (the "not found" error), and a JSON response of:

```
{
  "detail": "Item not found"
}
```

Tip

When raising an `HTTPException`, you can pass any value that can be converted to JSON as the parameter `detail`, not only `str`.

You could pass a `dict`, a `list`, etc.

They are handled automatically by **FastAPI** and converted to JSON.