---
id: python-return-types-https-docs-python-org-3-library-ctypes-html-ret-07786b1c
type: concept
title: Return types[¶](https://docs.python.org/3/library/ctypes.html#return-types
  "Link to this heading")
description: By default functions are assumed to return the C int type. Other
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Return types[¶](https://docs.python.org/3/library/ctypes.html#return-types "Link to this heading")

By default functions are assumed to return the C int type. Other
return types can be specified by setting the [`restype`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "ctypes._CFuncPtr.restype") attribute of the
function object.

The C prototype of `time()` is `time_t time(time_t *)`. Because `time_t`
might be of a different type than the default return type int, you should
specify the `restype` attribute:

```
>>> libc.time.restype = c_time_t
```

The argument types can be specified using [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes"):

```
>>> libc.time.argtypes = (POINTER(c_time_t),)
```

To call the function with a `NULL` pointer as first argument, use `None`:

```
>>> print(libc.time(None))
1150640792
```

Here is a more advanced example, it uses the `strchr()` function, which expects
a string pointer and a char, and returns a pointer to a string:

```
>>> strchr = libc.strchr
>>> strchr(b"abcdef", ord("d"))
8059983
>>> strchr.restype = c_char_p    # c_char_p is a pointer to a string
>>> strchr(b"abcdef", ord("d"))
b'def'
>>> print(strchr(b"abcdef", ord("x")))
None
>>>
```

If you want to avoid the [`ord("x")`](https://docs.python.org/3/library/functions.html#ord "ord") calls above, you can set the
[`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") attribute, and the second argument will be converted from a
single character Python bytes object into a C char:

```
>>> strchr.restype = c_char_p
>>> strchr.argtypes = [c_char_p, c_char]
>>> strchr(b"abcdef", b"d")
b'def'
>>> strchr(b"abcdef", b"def")
Traceback (most recent call last):
ctypes.ArgumentError: argument 2: TypeError: one character bytes, bytearray or integer expected
>>> print(strchr(b"abcdef", b"x"))
None
>>> strchr(b"abcdef", b"d")
b'def'
>>>
```

You can also use a callable Python object (a function or a class for example) as
the [`restype`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "ctypes._CFuncPtr.restype") attribute, if the foreign function returns an integer. The
callable will be called with the *integer* the C function returns, and the
result of this call will be used as the result of your function call. This is
useful to check for error return values and automatically raise an exception:

```
>>> GetModuleHandle = windll.kernel32.GetModuleHandleA
>>> def ValidHandle(value):
...     if value == 0:
...         raise WinError()
...     return value
...
>>>
>>> GetModuleHandle.restype = ValidHandle
>>> GetModuleHandle(None)
486539264
>>> GetModuleHandle("something silly")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in ValidHandle
OSError: [Errno 126] The specified module could not be found.
>>>
```

`WinError` is a function which will call Windows `FormatMessage()` api to
get the string representation of an error code, and *returns* an exception.
`WinError` takes an optional error code parameter, if no one is used, it calls
[`GetLastError()`](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "ctypes.GetLastError") to retrieve it.

Please note that a much more powerful error checking mechanism is available
through the [`errcheck`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "ctypes._CFuncPtr.errcheck") attribute;
see the reference manual for details.