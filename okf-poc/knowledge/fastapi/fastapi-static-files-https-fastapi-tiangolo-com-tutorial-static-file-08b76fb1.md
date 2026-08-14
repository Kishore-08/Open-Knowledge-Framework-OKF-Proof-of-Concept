---
id: fastapi-static-files-https-fastapi-tiangolo-com-tutorial-static-file-08b76fb1
type: concept
title: Static Files[¶](https://fastapi.tiangolo.com/tutorial/static-files/#static-files
description: You can serve static files automatically from a directory using `StaticFiles`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/static-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Static Files[¶](https://fastapi.tiangolo.com/tutorial/static-files/#static-files "Permanent link")

You can serve static files automatically from a directory using `StaticFiles`.

Tip

If you need to host a frontend, use `app.frontend()` instead, read about it in [Frontend](https://fastapi.tiangolo.com/tutorial/frontend/).

`app.frontend()` uses `StaticFiles` underneath, with several additional advantages for frontends, like handling client-side routing.