---
id: fastapi-background-tasks-https-fastapi-tiangolo-com-tutorial-backgro-3e17b7a1
type: concept
title: Background Tasks[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#back
description: You can define background tasks to be run *after* returning a response.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/background-tasks/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

# Background Tasks[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#background-tasks "Permanent link")

You can define background tasks to be run *after* returning a response.

This is useful for operations that need to happen after a request, but that the client doesn't really have to be waiting for the operation to complete before receiving the response.

This includes, for example:

- Email notifications sent after performing an action:
  - As connecting to an email server and sending an email tends to be "slow" (several seconds), you can return the response right away and send the email notification in the background.
- Processing data:
  - For example, let's say you receive a file that must go through a slow process, you can return a response of "Accepted" (HTTP 202) and process the file in the background.