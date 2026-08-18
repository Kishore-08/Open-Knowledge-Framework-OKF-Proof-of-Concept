---
id: fastapi-license-identifier-https-fastapi-tiangolo-com-tutorial-metad-afa173ff
type: concept
title: License identifier[¶](https://fastapi.tiangolo.com/tutorial/metadata/#license-identifier
  "Permanent link")
description: Since OpenAPI 3.1.0 and FastAPI 0.99.0, you can also set the `license_info`
  with an `identifier` instead of a `url`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/metadata/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## License identifier[¶](https://fastapi.tiangolo.com/tutorial/metadata/#license-identifier "Permanent link")

Since OpenAPI 3.1.0 and FastAPI 0.99.0, you can also set the `license_info` with an `identifier` instead of a `url`.

For example:

Python 3.10+

```
from fastapi import FastAPI

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.