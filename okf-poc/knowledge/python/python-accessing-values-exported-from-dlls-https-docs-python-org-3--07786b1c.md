---
id: python-accessing-values-exported-from-dlls-https-docs-python-org-3--07786b1c
type: concept
title: Accessing values exported from dlls[¶](https://docs.python.org/3/library/ctypes.html#accessing-values-exported-from-dlls
  "Link to this heading")
description: Some shared libraries not only export functions, they also export variables.
  An
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Accessing values exported from dlls[¶](https://docs.python.org/3/library/ctypes.html#accessing-values-exported-from-dlls "Link to this heading")

Some shared libraries not only export functions, they also export variables. An
example in the Python library itself is the [`Py_Version`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_Version "Py_Version"), Python
runtime version number encoded in a single constant integer.

`ctypes` can access values like this with the [`in_dll()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.in_dll "ctypes._CData.in_dll") class methods of
the type. *pythonapi* is a predefined symbol giving access to the Python C
api:

```
>>> version = ctypes.c_int.in_dll(ctypes.pythonapi, "Py_Version")
>>> print(hex(version.value))
0x30c00a0
```

An extended example which also demonstrates the use of pointers accesses the
[`PyImport_FrozenModules`](https://docs.python.org/3/c-api/import.html#c.PyImport_FrozenModules "PyImport_FrozenModules") pointer exported by Python.

Quoting the docs for that value:

> This pointer is initialized to point to an array of [`_frozen`](https://docs.python.org/3/c-api/import.html#c._frozen "_frozen")
> records, terminated by one whose members are all `NULL` or zero. When a frozen
> module is imported, it is searched in this table. Third-party code could play
> tricks with this to provide a dynamically created collection of frozen modules.

So manipulating this pointer could even prove useful. To restrict the example
size, we show only how this table can be read with `ctypes`:

```
>>> from ctypes import *
>>>
>>> class struct_frozen(Structure):
...     _fields_ = [("name", c_char_p),
...                 ("code", POINTER(c_ubyte)),
...                 ("size", c_int),
...                 ("get_code", POINTER(c_ubyte)),  # Function pointer
...                ]
...
>>>
```

We have defined the [`_frozen`](https://docs.python.org/3/c-api/import.html#c._frozen "_frozen") data type, so we can get the pointer
to the table:

```
>>> FrozenTable = POINTER(struct_frozen)
>>> table = FrozenTable.in_dll(pythonapi, "_PyImport_FrozenBootstrap")
>>>
```

Since `table` is a `pointer` to the array of `struct_frozen` records, we
can iterate over it, but we just have to make sure that our loop terminates,
because pointers have no size. Sooner or later it would probably crash with an
access violation or whatever, so it’s better to break out of the loop when we
hit the `NULL` entry:

```
>>> for item in table:
...     if item.name is None:
...         break
...     print(item.name.decode("ascii"), item.size)
...
_frozen_importlib 31764
_frozen_importlib_external 41499
zipimport 12345
>>>
```

The fact that standard Python has a frozen module and a frozen package
(indicated by the negative `size` member) is not well known, it is only used
for testing. Try it out with `import __hello__` for example.