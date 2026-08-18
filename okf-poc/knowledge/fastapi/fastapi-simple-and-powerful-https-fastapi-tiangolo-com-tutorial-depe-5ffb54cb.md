---
id: fastapi-simple-and-powerful-https-fastapi-tiangolo-com-tutorial-depe-5ffb54cb
type: concept
title: Simple and Powerful[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#simple-and-powerful
  "Permanent link")
description: Although the hierarchical dependency injection system is very simple
  to define and use, it's still very powerful.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Simple and Powerful[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#simple-and-powerful "Permanent link")

Although the hierarchical dependency injection system is very simple to define and use, it's still very powerful.

You can define dependencies that in turn can define dependencies themselves.

In the end, a hierarchical tree of dependencies is built, and the **Dependency Injection** system takes care of solving all these dependencies for you (and their sub-dependencies) and providing (injecting) the results at each step.

For example, let's say you have 4 API endpoints (*path operations*):

- `/items/public/`
- `/items/private/`
- `/users/{user_id}/activate`
- `/items/pro/`

then you could add different permission requirements for each of them just with dependencies and sub-dependencies:

```
graph TB

current_user(["current_user"])
active_user(["active_user"])
admin_user(["admin_user"])
paying_user(["paying_user"])

public["/items/public/"]
private["/items/private/"]
activate_user["/users/{user_id}/activate"]
pro_items["/items/pro/"]

current_user --> active_user
active_user --> admin_user
active_user --> paying_user

current_user --> public
active_user --> private
admin_user --> activate_user
paying_user --> pro_items
```