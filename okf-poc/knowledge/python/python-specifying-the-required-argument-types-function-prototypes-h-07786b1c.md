---
id: python-specifying-the-required-argument-types-function-prototypes-h-07786b1c
type: concept
title: Specifying the required argument types (function prototypes)[¶](https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes
  "Link to this heading")
description: It is possible to specify the required argument types of functions exported
  from
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Specifying the required argument types (function prototypes)[¶](https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes "Link to this heading")

It is possible to specify the required argument types of functions exported from
DLLs by setting the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") attribute.

[`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") must be a sequence of C data types (the `printf()` function is
probably not a good example here, because it takes a variable number and
different types of parameters depending on the format string, on the other hand
this is quite handy to experiment with this feature):

```
>>> printf.argtypes = [c_char_p, c_char_p, c_int, c_double]
>>> printf(b"String '%s', Int %d, Double %f\n", b"Hi", 10, 2.2)
String 'Hi', Int 10, Double 2.200000
37
>>>
```

Specifying a format protects against incompatible argument types (just as a
prototype for a C function), and tries to convert the arguments to valid types:

```
>>> printf(b"%d %d %d", 1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ctypes.ArgumentError: argument 2: TypeError: 'int' object cannot be interpreted as ctypes.c_char_p
>>> printf(b"%s %d %f\n", b"X", 2, 3)
X 2 3.000000
13
>>>
```

If you have defined your own classes which you pass to function calls, you have
to implement a [`from_param()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "ctypes._CData.from_param") class method for them to be able to use them
in the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") sequence. The `from_param()` class method receives
the Python object passed to the function call, it should do a typecheck or
whatever is needed to make sure this object is acceptable, and then return the
object itself, its `_as_parameter_` attribute, or whatever you want to
pass as the C function argument in this case. Again, the result should be an
integer, string, bytes, a `ctypes` instance, or an object with an
`_as_parameter_` attribute.