---
id: python-type-conversions-https-docs-python-org-3-library-ctypes-html-07786b1c
type: concept
title: Type conversions[¶](https://docs.python.org/3/library/ctypes.html#type-conversions
  "Link to this heading")
description: Usually, ctypes does strict type checking. This means, if you have
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Type conversions[¶](https://docs.python.org/3/library/ctypes.html#type-conversions "Link to this heading")

Usually, ctypes does strict type checking. This means, if you have
`POINTER(c_int)` in the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") list of a function or as the type of
a member field in a structure definition, only instances of exactly the same
type are accepted. There are some exceptions to this rule, where ctypes accepts
other objects. For example, you can pass compatible array instances instead of
pointer types. So, for `POINTER(c_int)`, ctypes accepts an array of c\_int:

```
>>> class Bar(Structure):
...     _fields_ = [("count", c_int), ("values", POINTER(c_int))]
...
>>> bar = Bar()
>>> bar.values = (c_int * 3)(1, 2, 3)
>>> bar.count = 3
>>> for i in range(bar.count):
...     print(bar.values[i])
...
1
2
3
>>>
```

In addition, if a function argument is explicitly declared to be a pointer type
(such as `POINTER(c_int)`) in [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes"), an object of the pointed
type (`c_int` in this case) can be passed to the function. ctypes will apply
the required [`byref()`](https://docs.python.org/3/library/ctypes.html#ctypes.byref "ctypes.byref") conversion in this case automatically.

To set a POINTER type field to `NULL`, you can assign `None`:

```
>>> bar.values = None
>>>
```

Sometimes you have instances of incompatible types. In C, you can cast one type
into another type. `ctypes` provides a [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast") function which can be
used in the same way. The `Bar` structure defined above accepts
`POINTER(c_int)` pointers or [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int") arrays for its `values` field,
but not instances of other types:

```
>>> bar.values = (c_byte * 4)()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: incompatible types, c_byte_Array_4 instance instead of LP_c_long instance
>>>
```

For these cases, the [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast") function is handy.

The [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast") function can be used to cast a ctypes instance into a pointer
to a different ctypes data type. `cast()` takes two parameters, a ctypes
object that is or can be converted to a pointer of some kind, and a ctypes
pointer type. It returns an instance of the second argument, which references
the same memory block as the first argument:

```
>>> a = (c_byte * 4)()
>>> cast(a, POINTER(c_int))
<ctypes.LP_c_long object at ...>
>>>
```

So, [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast") can be used to assign to the `values` field of `Bar` the
structure:

```
>>> bar = Bar()
>>> bar.values = cast((c_byte * 4)(), POINTER(c_int))
>>> print(bar.values[0])
0
>>>
```