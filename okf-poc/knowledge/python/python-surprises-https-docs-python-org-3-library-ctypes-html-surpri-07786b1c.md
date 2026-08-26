---
id: python-surprises-https-docs-python-org-3-library-ctypes-html-surpri-07786b1c
type: concept
title: Surprises[¶](https://docs.python.org/3/library/ctypes.html#surprises "Link
  to this heading")
description: There are some edges in `ctypes` where you might expect something other
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Surprises[¶](https://docs.python.org/3/library/ctypes.html#surprises "Link to this heading")

There are some edges in `ctypes` where you might expect something other
than what actually happens.

Consider the following example:

```
>>> from ctypes import *
>>> class POINT(Structure):
...     _fields_ = ("x", c_int), ("y", c_int)
...
>>> class RECT(Structure):
...     _fields_ = ("a", POINT), ("b", POINT)
...
>>> p1 = POINT(1, 2)
>>> p2 = POINT(3, 4)
>>> rc = RECT(p1, p2)
>>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
1 2 3 4
>>> # now swap the two points
>>> rc.a, rc.b = rc.b, rc.a
>>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
3 4 3 4
>>>
```

Hm. We certainly expected the last statement to print `3 4 1 2`. What
happened? Here are the steps of the `rc.a, rc.b = rc.b, rc.a` line above:

```
>>> temp0, temp1 = rc.b, rc.a
>>> rc.a = temp0
>>> rc.b = temp1
>>>
```

Note that `temp0` and `temp1` are objects still using the internal buffer of
the `rc` object above. So executing `rc.a = temp0` copies the buffer
contents of `temp0` into `rc` ‘s buffer. This, in turn, changes the
contents of `temp1`. So, the last assignment `rc.b = temp1`, doesn’t have
the expected effect.

Keep in mind that retrieving sub-objects from Structure, Unions, and Arrays
doesn’t *copy* the sub-object, instead it retrieves a wrapper object accessing
the root-object’s underlying buffer.

Another example that may behave differently from what one would expect is this:

```
>>> s = c_char_p()
>>> s.value = b"abc def ghi"
>>> s.value
b'abc def ghi'
>>> s.value is s.value
False
>>>
```

Note

Objects instantiated from [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p") can only have their value set to bytes
or integers.

Why is it printing `False`? ctypes instances are objects containing a memory
block plus some [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)s accessing the contents of the memory.
Storing a Python object in the memory block does not store the object itself,
instead the `contents` of the object is stored. Accessing the contents again
constructs a new Python object each time!