---
id: fastapi-caveat-https-fastapi-tiangolo-com-tutorial-background-tasks--3e17b7a1
type: concept
title: Caveat[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#caveat "Permanent
  link")
description: If you need to perform heavy background computation and you don't necessarily
  need it to be run by the same process (for example, you don't need to share memory,
  variables, etc), you might benefit fro
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/background-tasks/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Caveat[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#caveat "Permanent link")

If you need to perform heavy background computation and you don't necessarily need it to be run by the same process (for example, you don't need to share memory, variables, etc), you might benefit from using other bigger tools like [Celery](https://docs.celeryq.dev).

They tend to require more complex configurations, a message/job queue manager, like RabbitMQ or Redis, but they allow you to run background tasks in multiple processes, and especially, in multiple servers.

But if you need to access variables and objects from the same **FastAPI** app, or you need to perform small background tasks (like sending an email notification), you can simply just use `BackgroundTasks`.