---
id: fastapi-fastapi-plug-ins-https-fastapi-tiangolo-com-tutorial-depende-5ffb54cb
type: concept
title: '**FastAPI** plug-ins[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#fastapi-plug-ins
  "Permanent link")'
description: Integrations and "plug-ins" can be built using the **Dependency Injection**
  system. But in fact, there is actually **no need to create "plug-ins"**, as by using
  dependencies it's possible to declare a
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## **FastAPI** plug-ins[¶](https://fastapi.tiangolo.com/tutorial/dependencies/#fastapi-plug-ins "Permanent link")

Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using dependencies it's possible to declare an infinite number of integrations and interactions that become available to your *path operation functions*.

And dependencies can be created in a very simple and intuitive way that allows you to just import the Python packages you need, and integrate them with your API functions in a couple of lines of code, *literally*.

You will see examples of this in the next chapters, about relational and NoSQL databases, security, etc.