---
id: fastapi-update-the-app-with-multiple-models-https-fastapi-tiangolo-c-5b402114
type: concept
title: Update the App with Multiple Models[¶](https://fastapi.tiangolo.com/tutorial/sql-databases/#update-the-app-with-multiple-models
  "Permanent link")
description: Now let's **refactor** this app a bit to increase **security** and **versatility**.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/sql-databases/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Update the App with Multiple Models[¶](https://fastapi.tiangolo.com/tutorial/sql-databases/#update-the-app-with-multiple-models "Permanent link")

Now let's **refactor** this app a bit to increase **security** and **versatility**.

If you check the previous app, in the UI you can see that, up to now, it lets the client decide the `id` of the `Hero` to create. 😱

We shouldn't let that happen, they could overwrite an `id` we already have assigned in the DB. Deciding the `id` should be done by the **backend** or the **database**, **not by the client**.

Additionally, we create a `secret_name` for the hero, but so far, we are returning it everywhere, that's not very **secret**... 😅

We'll fix these things by adding a few **extra models**. Here's where SQLModel will shine. ✨