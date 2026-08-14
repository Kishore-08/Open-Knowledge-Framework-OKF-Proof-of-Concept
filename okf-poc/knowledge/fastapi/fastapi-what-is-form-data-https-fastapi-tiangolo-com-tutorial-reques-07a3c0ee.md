---
id: fastapi-what-is-form-data-https-fastapi-tiangolo-com-tutorial-reques-07a3c0ee
type: concept
title: What is "Form Data"[¶](https://fastapi.tiangolo.com/tutorial/request-files/#what-is-form-data
  "Permanent link")
description: The way HTML forms (`<form></form>`) send the data to the server normally
  uses a "special" encoding for that data, it's different from JSON.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/request-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## What is "Form Data"[¶](https://fastapi.tiangolo.com/tutorial/request-files/#what-is-form-data "Permanent link")

The way HTML forms (`<form></form>`) send the data to the server normally uses a "special" encoding for that data, it's different from JSON.

**FastAPI** will make sure to read that data from the right place instead of JSON.

Technical Details

Data from forms is normally encoded using the "media type" `application/x-www-form-urlencoded` when it doesn't include files.

But when the form includes files, it is encoded as `multipart/form-data`. If you use `File`, **FastAPI** will know it has to get the files from the correct part of the body.

If you want to read more about these encodings and form fields, head to the [MDN web docs for `POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST).

Warning

You can declare multiple `File` and `Form` parameters in a *path operation*, but you can't also declare `Body` fields that you expect to receive as JSON, as the request will have the body encoded using `multipart/form-data` instead of `application/json`.

This is not a limitation of **FastAPI**, it's part of the HTTP protocol.