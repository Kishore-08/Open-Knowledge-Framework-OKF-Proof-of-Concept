---
id: python-coroutine-utility-functions-https-docs-python-org-3-library--3209cdc1
type: concept
title: Coroutine Utility Functions[¶](https://docs.python.org/3/library/types.html#coroutine-utility-functions
  "Link to this heading")
description: types.coroutine(*gen\_func*)[¶](https://docs.python.org/3/library/types.html#types.coroutine
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/types.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Coroutine Utility Functions[¶](https://docs.python.org/3/library/types.html#coroutine-utility-functions "Link to this heading")

types.coroutine(*gen\_func*)[¶](https://docs.python.org/3/library/types.html#types.coroutine "Link to this definition")
:   This function transforms a [generator](https://docs.python.org/3/glossary.html#term-generator) function into a
    [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function) which returns a generator-based coroutine.
    The generator-based coroutine is still a [generator iterator](https://docs.python.org/3/glossary.html#term-generator-iterator),
    but is also considered to be a [coroutine](https://docs.python.org/3/glossary.html#term-coroutine) object and is
    [awaitable](https://docs.python.org/3/glossary.html#term-awaitable). However, it may not necessarily implement
    the [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__") method.

    If *gen\_func* is a generator function, it will be modified in-place.

    If *gen\_func* is not a generator function, it will be wrapped. If it
    returns an instance of [`collections.abc.Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator"), the instance
    will be wrapped in an *awaitable* proxy object. All other types
    of objects will be returned as is.

    Added in version 3.5.