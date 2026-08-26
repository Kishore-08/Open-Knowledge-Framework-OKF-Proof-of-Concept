---
id: python-passing-pointers-or-passing-parameters-by-reference-https-do-07786b1c
type: concept
title: 'Passing pointers (or: passing parameters by reference)[¶](https://docs.python.org/3/library/ctypes.html#passing-pointers-or-passing-parameters-by-reference
  "Link to this heading")'
description: Sometimes a C api function expects a *pointer* to a data type as parameter,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Passing pointers (or: passing parameters by reference)[¶](https://docs.python.org/3/library/ctypes.html#passing-pointers-or-passing-parameters-by-reference "Link to this heading")

Sometimes a C api function expects a *pointer* to a data type as parameter,
probably to write into the corresponding location, or if the data is too large
to be passed by value. This is also known as *passing parameters by reference*.

`ctypes` exports the [`byref()`](https://docs.python.org/3/library/ctypes.html#ctypes.byref "ctypes.byref") function which is used to pass parameters
by reference. The same effect can be achieved with the [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer") function,
although `pointer()` does a lot more work since it constructs a real pointer
object, so it is faster to use `byref()` if you don’t need the pointer
object in Python itself:

```
>>> i = c_int()
>>> f = c_float()
>>> s = create_string_buffer(b'\000' * 32)
>>> print(i.value, f.value, repr(s.value))
0 0.0 b''
>>> libc.sscanf(b"1 3.14 Hello", b"%d %f %s",
...             byref(i), byref(f), s)
3
>>> print(i.value, f.value, repr(s.value))
1 3.1400001049 b'Hello'
>>>
```