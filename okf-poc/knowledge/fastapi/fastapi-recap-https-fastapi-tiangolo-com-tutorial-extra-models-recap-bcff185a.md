---
id: fastapi-recap-https-fastapi-tiangolo-com-tutorial-extra-models-recap-bcff185a
type: concept
title: Recap[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#recap "Permanent
  link")
description: Use multiple Pydantic models and inherit freely for each case.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/extra-models/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Recap[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#recap "Permanent link")

Use multiple Pydantic models and inherit freely for each case.

You don't need to have a single data model per entity if that entity must be able to have different "states". The **user** "entity" is an example, with states that include `password`, `password_hash`, or no password.