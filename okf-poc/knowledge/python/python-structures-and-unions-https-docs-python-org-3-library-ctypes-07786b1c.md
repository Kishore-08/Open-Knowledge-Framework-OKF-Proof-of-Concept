---
id: python-structures-and-unions-https-docs-python-org-3-library-ctypes-07786b1c
type: concept
title: Structures and unions[¶](https://docs.python.org/3/library/ctypes.html#structures-and-unions
  "Link to this heading")
description: Structures and unions must derive from the [`Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure
  "ctypes.Structure") and [`Union`](https://docs.python.org/3/library/ctypes.html#
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Structures and unions[¶](https://docs.python.org/3/library/ctypes.html#structures-and-unions "Link to this heading")

Structures and unions must derive from the [`Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure") and [`Union`](https://docs.python.org/3/library/ctypes.html#ctypes.Union "ctypes.Union")
base classes which are defined in the `ctypes` module. Each subclass must
define a [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") attribute. `_fields_` must be a list of
*2-tuples*, containing a *field name* and a *field type*.

The field type must be a `ctypes` type like [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int"), or any other
derived `ctypes` type: structure, union, array, pointer.

Here is a simple example of a POINT structure, which contains two integers named
*x* and *y*, and also shows how to initialize a structure in the constructor:

```
>>> from ctypes import *
>>> class POINT(Structure):
...     _fields_ = [("x", c_int),
...                 ("y", c_int)]
...
>>> point = POINT(10, 20)
>>> print(point.x, point.y)
10 20
>>> point = POINT(y=5)
>>> print(point.x, point.y)
0 5
>>> POINT(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: too many initializers
>>>
```

You can, however, build much more complicated structures. A structure can
itself contain other structures by using a structure as a field type.

Here is a RECT structure which contains two POINTs named *upperleft* and
*lowerright*:

```
>>> class RECT(Structure):
...     _fields_ = [("upperleft", POINT),
...                 ("lowerright", POINT)]
...
>>> rc = RECT(point)
>>> print(rc.upperleft.x, rc.upperleft.y)
0 5
>>> print(rc.lowerright.x, rc.lowerright.y)
0 0
>>>
```

Nested structures can also be initialized in the constructor in several ways:

```
>>> r = RECT(POINT(1, 2), POINT(3, 4))
>>> r = RECT((1, 2), (3, 4))
```

Field [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)s can be retrieved from the *class*, they are useful
for debugging because they can provide useful information.
See [`CField`](https://docs.python.org/3/library/ctypes.html#ctypes.CField "ctypes.CField"):

```
>>> POINT.x
<ctypes.CField 'x' type=c_int, ofs=0, size=4>
>>> POINT.y
<ctypes.CField 'y' type=c_int, ofs=4, size=4>
>>>
```

Warning

`ctypes` does not support passing unions or structures with bit-fields
to functions by value. While this may work on 32-bit x86, it’s not
guaranteed by the library to work in the general case. Unions and
structures with bit-fields should always be passed to functions by pointer.