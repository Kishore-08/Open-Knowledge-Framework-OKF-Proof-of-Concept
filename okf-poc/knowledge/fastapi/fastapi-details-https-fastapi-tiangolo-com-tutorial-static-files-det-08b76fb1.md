---
id: fastapi-details-https-fastapi-tiangolo-com-tutorial-static-files-det-08b76fb1
type: concept
title: Details[¶](https://fastapi.tiangolo.com/tutorial/static-files/#details "Permanent
  link")
description: The first `"/static"` refers to the sub-path this "sub-application" will
  be "mounted" on. So, any path that starts with `"/static"` will be handled by it.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/static-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Details[¶](https://fastapi.tiangolo.com/tutorial/static-files/#details "Permanent link")

The first `"/static"` refers to the sub-path this "sub-application" will be "mounted" on. So, any path that starts with `"/static"` will be handled by it.

The `directory="static"` refers to the name of the directory that contains your static files.

The `name="static"` gives it a name that can be used internally by **FastAPI**.

All these parameters can be different than "`static`", adjust them to the needs and specific details of your own application.