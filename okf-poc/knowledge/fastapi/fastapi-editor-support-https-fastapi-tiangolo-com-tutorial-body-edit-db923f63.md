---
id: fastapi-editor-support-https-fastapi-tiangolo-com-tutorial-body-edit-db923f63
type: concept
title: Editor support[¶](https://fastapi.tiangolo.com/tutorial/body/#editor-support
  "Permanent link")
description: 'In your editor, inside your function you will get type hints and completion
  everywhere (this wouldn''t happen if you received a `dict` instead of a Pydantic
  model):'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/body/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Editor support[¶](https://fastapi.tiangolo.com/tutorial/body/#editor-support "Permanent link")

In your editor, inside your function you will get type hints and completion everywhere (this wouldn't happen if you received a `dict` instead of a Pydantic model):

You also get error checks for incorrect type operations:

This is not by chance, the whole framework was built around that design.

And it was thoroughly tested at the design phase, before any implementation, to ensure it would work with all the editors.

There were even some changes to Pydantic itself to support this.

The previous screenshots were taken with [Visual Studio Code](https://code.visualstudio.com).

But you would get the same editor support with [PyCharm](https://www.jetbrains.com/pycharm/) and most of the other Python editors:

Tip

If you use [PyCharm](https://www.jetbrains.com/pycharm/) as your editor, you can use the [Pydantic PyCharm Plugin](https://github.com/koxudaxi/pydantic-pycharm-plugin/).

It improves editor support for Pydantic models, with:

- auto-completion
- type checks
- refactoring
- searching
- inspections