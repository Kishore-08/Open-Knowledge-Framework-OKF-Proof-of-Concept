---
id: fastapi-add-the-background-task-https-fastapi-tiangolo-com-tutorial--3e17b7a1
type: concept
title: Add the background task[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#add-the-background-task
  "Permanent link")
description: 'Inside of your *path operation function*, pass your task function to
  the *background tasks* object with the method `.add_task()`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/background-tasks/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Add the background task[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#add-the-background-task "Permanent link")

Inside of your *path operation function*, pass your task function to the *background tasks* object with the method `.add_task()`:

Python 3.10+

```
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
```

`.add_task()` receives as arguments:

- A task function to be run in the background (`write_notification`).
- Any sequence of arguments that should be passed to the task function in order (`email`).
- Any keyword arguments that should be passed to the task function (`message="some notification"`).