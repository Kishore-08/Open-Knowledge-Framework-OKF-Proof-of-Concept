---
id: fastapi-type-annotations-and-tooling-https-fastapi-tiangolo-com-tuto-188ea97b
type: concept
title: Type Annotations and Tooling[¶](https://fastapi.tiangolo.com/tutorial/response-model/#type-annotations-and-tooling
  "Permanent link")
description: First let's see how editors, mypy and other tools would see this.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Type Annotations and Tooling[¶](https://fastapi.tiangolo.com/tutorial/response-model/#type-annotations-and-tooling "Permanent link")

First let's see how editors, mypy and other tools would see this.

`BaseUser` has the base fields. Then `UserIn` inherits from `BaseUser` and adds the `password` field, so, it will include all the fields from both models.

We annotate the function return type as `BaseUser`, but we are actually returning a `UserIn` instance.

The editor, mypy, and other tools won't complain about this because, in typing terms, `UserIn` is a subclass of `BaseUser`, which means it's a *valid* type when what is expected is anything that is a `BaseUser`.