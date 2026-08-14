---
id: fastapi-add-extra-information-https-fastapi-tiangolo-com-tutorial-bo-f7417381
type: concept
title: Add extra information[¶](https://fastapi.tiangolo.com/tutorial/body-fields/#add-extra-information
  "Permanent link")
description: You can declare extra information in `Field`, `Query`, `Body`, etc. And
  it will be included in the generated JSON Schema.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body-fields/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Add extra information[¶](https://fastapi.tiangolo.com/tutorial/body-fields/#add-extra-information "Permanent link")

You can declare extra information in `Field`, `Query`, `Body`, etc. And it will be included in the generated JSON Schema.

You will learn more about adding extra information later in the docs, when learning to declare examples.

Warning

Extra keys passed to `Field` will also be present in the resulting OpenAPI schema for your application.
As these keys may not necessarily be part of the OpenAPI specification, some OpenAPI tools, for example [the OpenAPI validator](https://validator.swagger.io/), may not work with your generated schema.