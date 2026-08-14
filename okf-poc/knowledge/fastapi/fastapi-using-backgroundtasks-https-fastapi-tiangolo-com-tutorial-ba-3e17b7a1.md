---
id: fastapi-using-backgroundtasks-https-fastapi-tiangolo-com-tutorial-ba-3e17b7a1
type: concept
title: Using `BackgroundTasks`[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#using-backgroundtasks
  "Permanent link")
description: 'First, import `BackgroundTasks` and define a parameter in your *path
  operation function* with a type declaration of `BackgroundTasks`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/background-tasks/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Using `BackgroundTasks`[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#using-backgroundtasks "Permanent link")

First, import `BackgroundTasks` and define a parameter in your *path operation function* with a type declaration of `BackgroundTasks`:

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

**FastAPI** will create the object of type `BackgroundTasks` for you and pass it as that parameter.