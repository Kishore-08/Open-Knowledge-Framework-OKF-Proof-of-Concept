---
id: python-partial-https-docs-python-org-3-library-functools-html-funct-1cd9df78
type: concept
title: '[`partial`](https://docs.python.org/3/library/functools.html#functools.partial
  "functools.partial") Objects[¶](https://docs.python.org/3/library/functools.html#partial-objects
  "Link to this heading")'
description: '[`partial`](https://docs.python.org/3/library/functools.html#functools.partial
  "functools.partial") objects are callable objects created by [`partial()`](https://docs.python.org/3/library/functools.ht'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/functools.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## [`partial`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") Objects[¶](https://docs.python.org/3/library/functools.html#partial-objects "Link to this heading")

[`partial`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") objects are callable objects created by [`partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial"). They
have three read-only attributes:

partial.func[¶](https://docs.python.org/3/library/functools.html#functools.partial.func "Link to this definition")
:   A callable object or function. Calls to the [`partial`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") object will be
    forwarded to [`func`](https://docs.python.org/3/library/functools.html#functools.partial.func "functools.partial.func") with new arguments and keywords.

partial.args[¶](https://docs.python.org/3/library/functools.html#functools.partial.args "Link to this definition")
:   The leftmost positional arguments that will be prepended to the positional
    arguments provided to a [`partial`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") object call.

partial.keywords[¶](https://docs.python.org/3/library/functools.html#functools.partial.keywords "Link to this definition")
:   The keyword arguments that will be supplied when the [`partial`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") object is
    called.

[`partial`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") objects are like [function objects](https://docs.python.org/3/reference/datamodel.html#user-defined-funcs) in that they are
callable, weak referenceable, and can have attributes. There are some important
differences. For instance, the [`__name__`](https://docs.python.org/3/library/stdtypes.html#definition.__name__ "definition.__name__") and [`__doc__`](https://docs.python.org/3/library/stdtypes.html#definition.__doc__ "definition.__doc__") attributes
are not created automatically.