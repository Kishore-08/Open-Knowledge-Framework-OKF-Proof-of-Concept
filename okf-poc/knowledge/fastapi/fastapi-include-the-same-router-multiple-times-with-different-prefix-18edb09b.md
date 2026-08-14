---
id: fastapi-include-the-same-router-multiple-times-with-different-prefix-18edb09b
type: concept
title: Include the same router multiple times with different `prefix`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-same-router-multiple-times-with-different-prefix
  "Permanent link")
description: You can also use `.include_router()` multiple times with the *same* router
  using different prefixes.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/bigger-applications/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Include the same router multiple times with different `prefix`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-same-router-multiple-times-with-different-prefix "Permanent link")

You can also use `.include_router()` multiple times with the *same* router using different prefixes.

This could be useful, for example, to expose the same API under different prefixes, e.g. `/api/v1` and `/api/latest`.

This is an advanced usage that you might not really need, but it's there in case you do.