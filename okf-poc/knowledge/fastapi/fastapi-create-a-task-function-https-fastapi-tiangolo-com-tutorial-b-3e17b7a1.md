---
id: fastapi-create-a-task-function-https-fastapi-tiangolo-com-tutorial-b-3e17b7a1
type: concept
title: Create a task function[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#create-a-task-function
  "Permanent link")
description: Create a function to be run as the background task.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/background-tasks/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Create a task function[¶](https://fastapi.tiangolo.com/tutorial/background-tasks/#create-a-task-function "Permanent link")

Create a function to be run as the background task.

It is just a standard function that can receive parameters.

It can be an `async def` or normal `def` function, **FastAPI** will know how to handle it correctly.

In this case, the task function will write to a file (simulating sending an email).

And as the write operation doesn't use `async` and `await`, we define the function with normal `def`:

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