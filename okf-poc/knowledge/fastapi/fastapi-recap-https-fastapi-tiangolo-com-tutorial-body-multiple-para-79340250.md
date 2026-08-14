---
id: fastapi-recap-https-fastapi-tiangolo-com-tutorial-body-multiple-para-79340250
type: concept
title: Recap[¶](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#recap
  "Permanent link")
description: You can add multiple body parameters to your *path operation function*,
  even though a request can only have a single body.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-multiple-params/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Recap[¶](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#recap "Permanent link")

You can add multiple body parameters to your *path operation function*, even though a request can only have a single body.

But **FastAPI** will handle it, give you the correct data in your function, and validate and document the correct schema in the *path operation*.

You can also declare singular values to be received as part of the body.

And you can instruct **FastAPI** to embed the body in a key even when there is only a single parameter declared.