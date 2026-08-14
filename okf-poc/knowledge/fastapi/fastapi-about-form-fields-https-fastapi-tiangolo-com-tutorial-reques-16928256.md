---
id: fastapi-about-form-fields-https-fastapi-tiangolo-com-tutorial-reques-16928256
type: concept
title: About "Form Fields"[¶](https://fastapi.tiangolo.com/tutorial/request-forms/#about-form-fields
  "Permanent link")
description: The way HTML forms (`<form></form>`) send the data to the server normally
  uses a "special" encoding for that data, it's different from JSON.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-forms/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## About "Form Fields"[¶](https://fastapi.tiangolo.com/tutorial/request-forms/#about-form-fields "Permanent link")

The way HTML forms (`<form></form>`) send the data to the server normally uses a "special" encoding for that data, it's different from JSON.

**FastAPI** will make sure to read that data from the right place instead of JSON.

Technical Details

Data from forms is normally encoded using the "media type" `application/x-www-form-urlencoded`.

But when the form includes files, it is encoded as `multipart/form-data`. You'll read about handling files in the next chapter.

If you want to read more about these encodings and form fields, head to the [MDN web docs for `POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST).

Warning

You can declare multiple `Form` parameters in a *path operation*, but you can't also declare `Body` fields that you expect to receive as JSON, as the request will have the body encoded using `application/x-www-form-urlencoded` instead of `application/json`.

This is not a limitation of **FastAPI**, it's part of the HTTP protocol.

## Recap[¶](https://fastapi.tiangolo.com/tutorial/request-forms/#recap "Permanent link")

Use `Form` to declare form data input parameters.