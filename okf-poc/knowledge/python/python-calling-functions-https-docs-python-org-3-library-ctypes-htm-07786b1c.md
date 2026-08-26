---
id: python-calling-functions-https-docs-python-org-3-library-ctypes-htm-07786b1c
type: concept
title: Calling functions[¶](https://docs.python.org/3/library/ctypes.html#calling-functions
  "Link to this heading")
description: You can call these functions like any other Python callable. This example
  uses
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Calling functions[¶](https://docs.python.org/3/library/ctypes.html#calling-functions "Link to this heading")

You can call these functions like any other Python callable. This example uses
the `rand()` function, which takes no arguments and returns a pseudo-random integer:

```
>>> print(libc.rand())
1804289383
```

On Windows, you can call the `GetModuleHandleA()` function, which returns a win32 module
handle (passing `None` as single argument to call it with a `NULL` pointer):

```
>>> print(hex(windll.kernel32.GetModuleHandleA(None)))
0x1d000000
>>>
```

[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised when you call an `stdcall` function with the
`cdecl` calling convention, or vice versa:

```
>>> cdll.kernel32.GetModuleHandleA(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Procedure probably called with not enough arguments (4 bytes missing)
>>>

>>> windll.msvcrt.printf(b"spam")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Procedure probably called with too many arguments (4 bytes in excess)
>>>
```

To find out the correct calling convention you have to look into the C header
file or the documentation for the function you want to call.

On Windows, `ctypes` uses win32 structured exception handling to prevent
crashes from general protection faults when functions are called with invalid
argument values:

```
>>> windll.kernel32.GetModuleHandleA(32)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: exception: access violation reading 0x00000020
>>>
```

The [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.") module can help debug crashes,
such as segmentation faults produced by erroneous C library calls.

`None`, integers, bytes objects and (unicode) strings are the only native
Python objects that can directly be used as parameters in these function calls.
`None` is passed as a C `NULL` pointer, bytes objects and strings are passed
as pointer to the memory block that contains their data (char\* or
wchar\_t\*). Python integers are passed as the platform’s default C
int type, their value is masked to fit into the C type.

Before we move on calling functions with other parameter types, we have to learn
more about `ctypes` data types.