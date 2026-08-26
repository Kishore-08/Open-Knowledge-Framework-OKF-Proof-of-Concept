---
id: python-types-dynamic-type-creation-and-names-for-built-in-types-htt-3209cdc1
type: concept
title: '`types` — Dynamic type creation and names for built-in types[¶](https://docs.pyt'
description: '**Source code:** [Lib/types.py](https://github.com/python/cpython/tree/3.14/Lib/types.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/types.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `types` — Dynamic type creation and names for built-in types[¶](https://docs.python.org/3/library/types.html#module-types "Link to this heading")

**Source code:** [Lib/types.py](https://github.com/python/cpython/tree/3.14/Lib/types.py)

---

This module defines utility functions to assist in dynamic creation of
new types.

It also defines names for some object types that are used by the standard
Python interpreter, but not exposed as builtins like [`int`](https://docs.python.org/3/library/functions.html#int "int") or
[`str`](https://docs.python.org/3/library/stdtypes.html#str "str") are.

Finally, it provides some additional type-related utility classes and functions
that are not fundamental enough to be builtins.