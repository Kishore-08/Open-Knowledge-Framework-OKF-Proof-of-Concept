---
id: python-foreign-functions-https-docs-python-org-3-library-ctypes-htm-07786b1c
type: concept
title: Foreign functions[¶](https://docs.python.org/3/library/ctypes.html#foreign-functions
  "Link to this heading")
description: As explained in the previous section, foreign functions can be accessed
  as
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Foreign functions[¶](https://docs.python.org/3/library/ctypes.html#foreign-functions "Link to this heading")

As explained in the previous section, foreign functions can be accessed as
attributes of loaded shared libraries. The function objects created in this way
by default accept any number of arguments, accept any ctypes data instances as
arguments, and return the default result type specified by the library loader.

They are instances of a private local class `_FuncPtr` (not exposed
in `ctypes`) which inherits from the private [`_CFuncPtr`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr "ctypes._CFuncPtr") class:

```
>>> import ctypes
>>> lib = ctypes.CDLL(None)
>>> issubclass(lib._FuncPtr, ctypes._CFuncPtr)
True
>>> lib._FuncPtr is ctypes._CFuncPtr
False
```

*class* ctypes.\_CFuncPtr[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr "Link to this definition")
:   Base class for C callable foreign functions.

    Instances of foreign functions are also C compatible data types; they
    represent C function pointers.

    This behavior can be customized by assigning to special attributes of the
    foreign function object.

    restype[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "Link to this definition")
    :   Assign a ctypes type to specify the result type of the foreign function.
        Use `None` for void, a function not returning anything.

        It is possible to assign a callable Python object that is not a ctypes
        type, in this case the function is assumed to return a C int, and
        the callable will be called with this integer, allowing further
        processing or error checking. Using this is deprecated, for more flexible
        post processing or error checking use a ctypes data type as
        `restype` and assign a callable to the [`errcheck`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "ctypes._CFuncPtr.errcheck") attribute.

    argtypes[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "Link to this definition")
    :   Assign a tuple of ctypes types to specify the argument types that the
        function accepts. Functions using the `stdcall` calling convention can
        only be called with the same number of arguments as the length of this
        tuple; functions using the C calling convention accept additional,
        unspecified arguments as well.

        When a foreign function is called, each actual argument is passed to the
        [`from_param()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "ctypes._CData.from_param") class method of the items in the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
        tuple, this method allows adapting the actual argument to an object that
        the foreign function accepts. For example, a [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p") item in
        the `argtypes` tuple will convert a string passed as argument into
        a bytes object using ctypes conversion rules.

        New: It is now possible to put items in argtypes which are not ctypes
        types, but each item must have a [`from_param()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "ctypes._CData.from_param") method which returns a
        value usable as argument (integer, string, ctypes instance). This allows
        defining adapters that can adapt custom objects as function parameters.

    errcheck[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "Link to this definition")
    :   Assign a Python function or another callable to this attribute. The
        callable will be called with three or more arguments:

        callable(*result*, *func*, *arguments*)
        :   *result* is what the foreign function returns, as specified by the
            `restype` att