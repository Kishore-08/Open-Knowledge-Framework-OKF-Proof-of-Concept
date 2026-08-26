---
id: python-variable-sized-data-types-https-docs-python-org-3-library-ct-07786b1c
type: concept
title: Variable-sized data types[¶](https://docs.python.org/3/library/ctypes.html#variable-sized-data-types
  "Link to this heading")
description: '`ctypes` provides some support for variable-sized arrays and structures.'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Variable-sized data types[¶](https://docs.python.org/3/library/ctypes.html#variable-sized-data-types "Link to this heading")

`ctypes` provides some support for variable-sized arrays and structures.

The [`resize()`](https://docs.python.org/3/library/ctypes.html#ctypes.resize "ctypes.resize") function can be used to resize the memory buffer of an
existing ctypes object. The function takes the object as first argument, and
the requested size in bytes as the second argument. The memory block cannot be
made smaller than the natural memory block specified by the objects type, a
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if this is tried:

```
>>> short_array = (c_short * 4)()
>>> print(sizeof(short_array))
8
>>> resize(short_array, 4)
Traceback (most recent call last):
    ...
ValueError: minimum size is 8
>>> resize(short_array, 32)
>>> sizeof(short_array)
32
>>> sizeof(type(short_array))
8
>>>
```

This is nice and fine, but how would one access the additional elements
contained in this array? Since the type still only knows about 4 elements, we
get errors accessing other elements:

```
>>> short_array[:]
[0, 0, 0, 0]
>>> short_array[7]
Traceback (most recent call last):
    ...
IndexError: invalid index
>>>
```

Another way to use variable-sized data types with `ctypes` is to use the
dynamic nature of Python, and (re-)define the data type after the required size
is already known, on a case by case basis.

## ctypes reference[¶](https://docs.python.org/3/library/ctypes.html#ctypes-reference "Link to this heading")