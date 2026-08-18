---
id: fastapi-editor-support-everywhere-https-fastapi-tiangolo-com-tutoria-99d5900d
type: concept
title: Editor support everywhere[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#editor-support-everywhere
  "Permanent link")
description: And you get editor support everywhere.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-nested-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Editor support everywhere[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#editor-support-everywhere "Permanent link")

And you get editor support everywhere.

Even for items inside of lists:

You couldn't get this kind of editor support if you were working directly with `dict` instead of Pydantic models.

But you don't have to worry about them either, incoming dicts are converted automatically and your output is converted automatically to JSON too.