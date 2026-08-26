---
id: python-incomplete-types-https-docs-python-org-3-library-ctypes-html-07786b1c
type: concept
title: Incomplete Types[¶](https://docs.python.org/3/library/ctypes.html#incomplete-types
  "Link to this heading")
description: '*Incomplete Types* are structures, unions or arrays whose members are
  not yet'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Incomplete Types[¶](https://docs.python.org/3/library/ctypes.html#incomplete-types "Link to this heading")

*Incomplete Types* are structures, unions or arrays whose members are not yet
specified. In C, they are specified by forward declarations, which are defined
later:

```
struct cell; /* forward declaration */

struct cell {
    char *name;
    struct cell *next;
};
```

The straightforward translation into ctypes code would be this, but it does not
work:

```
>>> class cell(Structure):
...     _fields_ = [("name", c_char_p),
...                 ("next", POINTER(cell))]
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in cell
NameError: name 'cell' is not defined
>>>
```

because the new `class cell` is not available in the class statement itself.
In `ctypes`, we can define the `cell` class and set the
[`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") attribute later, after the class statement:

```
>>> from ctypes import *
>>> class cell(Structure):
...     pass
...
>>> cell._fields_ = [("name", c_char_p),
...                  ("next", POINTER(cell))]
>>>
```

Let’s try it. We create two instances of `cell`, and let them point to each
other, and finally follow the pointer chain a few times:

```
>>> c1 = cell()
>>> c1.name = b"foo"
>>> c2 = cell()
>>> c2.name = b"bar"
>>> c1.next = pointer(c2)
>>> c2.next = pointer(c1)
>>> p = c1
>>> for i in range(8):
...     print(p.name, end=" ")
...     p = p.next[0]
...
foo bar foo bar foo bar foo bar
>>>
```