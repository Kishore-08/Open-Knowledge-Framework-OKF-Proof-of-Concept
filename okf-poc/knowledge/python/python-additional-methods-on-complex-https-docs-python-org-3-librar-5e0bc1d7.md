---
id: python-additional-methods-on-complex-https-docs-python-org-3-librar-5e0bc1d7
type: concept
title: Additional Methods on Complex[¶](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-complex
  "Link to this heading")
description: The `complex` type implements the [`numbers.Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex
  "numbers.Complex")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Additional Methods on Complex[¶](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-complex "Link to this heading")

The `complex` type implements the [`numbers.Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex")
[abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class).
`complex` also has the following additional methods.

*classmethod* complex.from\_number(*x*)[¶](https://docs.python.org/3/library/stdtypes.html#complex.from_number "Link to this definition")
:   Class method to convert a number to a complex number.

    For a general Python object `x`, `complex.from_number(x)` delegates to
    `x.__complex__()`. If [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__") is not defined then it falls back
    to [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__"). If `__float__()` is not defined then it falls back
    to [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__").

    Added in version 3.14.