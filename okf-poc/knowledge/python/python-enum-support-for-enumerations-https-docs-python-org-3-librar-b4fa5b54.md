---
id: python-enum-support-for-enumerations-https-docs-python-org-3-librar-b4fa5b54
type: concept
title: '`enum` — Support for enumerations[¶](https://docs.python.org/3/library/enum.html'
description: Added in version 3.4.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/enum.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `enum` — Support for enumerations[¶](https://docs.python.org/3/library/enum.html#module-enum "Link to this heading")

Added in version 3.4.

**Source code:** [Lib/enum.py](https://github.com/python/cpython/tree/3.14/Lib/enum.py)

---

An enumeration:

- is a set of symbolic names (members) bound to unique values
- can be iterated over to return its canonical (i.e. non-alias) members in
  definition order
- uses *call* syntax to return members by value
- uses *index* syntax to return members by name

Enumerations are created either by using [`class`](https://docs.python.org/3/reference/compound_stmts.html#class) syntax, or by
using function-call syntax:

```
>>> from enum import Enum

>>> # class syntax
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3

>>> # functional syntax
>>> Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])
```

Even though we can use [`class`](https://docs.python.org/3/reference/compound_stmts.html#class) syntax to create Enums, Enums
are not normal Python classes. See
[How are Enums different?](https://docs.python.org/3/howto/enum.html#enum-class-differences) for more details.

Note

Nomenclature

- The class `Color` is an *enumeration* (or *enum*)
- The attributes `Color.RED`, `Color.GREEN`, etc., are
  *enumeration members* (or *members*) and are functionally constants.
- The enum members have *names* and *values* (the name of
  `Color.RED` is `RED`, the value of `Color.BLUE` is
  `3`, etc.)

---