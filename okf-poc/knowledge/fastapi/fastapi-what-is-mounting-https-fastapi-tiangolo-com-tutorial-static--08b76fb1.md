---
id: fastapi-what-is-mounting-https-fastapi-tiangolo-com-tutorial-static--08b76fb1
type: concept
title: What is "Mounting"[¶](https://fastapi.tiangolo.com/tutorial/static-files/#what-is-mounting
  "Permanent link")
description: '"Mounting" means adding a complete "independent" application in a specific
  path, that then takes care of handling all the sub-paths.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/static-files/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### What is "Mounting"[¶](https://fastapi.tiangolo.com/tutorial/static-files/#what-is-mounting "Permanent link")

"Mounting" means adding a complete "independent" application in a specific path, that then takes care of handling all the sub-paths.

This is different from using an `APIRouter` as a mounted application is completely independent. The OpenAPI and docs from your main application won't include anything from the mounted application, etc.

You can read more about this in the [Advanced User Guide](https://fastapi.tiangolo.com/advanced/).