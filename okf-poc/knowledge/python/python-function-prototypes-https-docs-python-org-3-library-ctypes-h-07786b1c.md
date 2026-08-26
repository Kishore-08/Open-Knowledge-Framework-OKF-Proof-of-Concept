---
id: python-function-prototypes-https-docs-python-org-3-library-ctypes-h-07786b1c
type: concept
title: Function prototypes[¶](https://docs.python.org/3/library/ctypes.html#function-prototypes
  "Link to this heading")
description: Foreign functions can also be created by instantiating function prototypes.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Function prototypes[¶](https://docs.python.org/3/library/ctypes.html#function-prototypes "Link to this heading")

Foreign functions can also be created by instantiating function prototypes.
Function prototypes are similar to function prototypes in C; they describe a
function (return type, argument types, calling convention) without defining an
implementation. The factory functions must be called with the desired result
type and the argument types of the function, and can be used as decorator
factories, and as such, be applied to functions through the `@wrapper` syntax.
See [Callback functions](https://docs.python.org/3/library/ctypes.html#ctypes-callback-functions) for examples.

ctypes.CFUNCTYPE(*restype*, *\*argtypes*, *use\_errno=False*, *use\_last\_error=False*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE "Link to this definition")
:   The returned function prototype creates functions that use the standard C
    calling convention. The function will release the GIL during the call. If
    *use\_errno* is set to true, the ctypes private copy of the system
    [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.") variable is exchanged with the real `errno` value before
    and after the call; *use\_last\_error* does the same for the Windows error
    code.

ctypes.WINFUNCTYPE(*restype*, *\*argtypes*, *use\_errno=False*, *use\_last\_error=False*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.WINFUNCTYPE "Link to this definition")
:   The returned function prototype creates functions that use the
    `stdcall` calling convention. The function will
    release the GIL during the call. *use\_errno* and *use\_last\_error* have the
    same meaning as above.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Windows

ctypes.PYFUNCTYPE(*restype*, *\*argtypes*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.PYFUNCTYPE "Link to this definition")
:   The returned function prototype creates functions that use the Python calling
    convention. The function will *not* release the GIL during the call.

Function prototypes created by these factory functions can be instantiated in
different ways, depending on the type and number of the parameters in the call:

prototype(*address*)
:   Returns a foreign function at the specified address which must be an integer.

prototype(*callable*)
:   Create a C callable function (a callback function) from a Python *callable*.

prototype(*func\_spec*[, *paramflags*])
:   Returns a foreign function exported by a shared library. *func\_spec* must
    be a 2-tuple `(name_or_ordinal, library)`. The first item is the name of
    the exported function as string, or the ordinal of the exported function
    as small integer. The second item is the shared library instance.

prototype(*vtbl\_index*, *name*[, *paramflags*[, *iid*]])
:   Returns a foreign function that will call a COM method. *vtbl\_index* is
    the index into the virtual function table, a small non-negative
    integer. *name* is name of the COM method. *iid* is an optional pointer to
    the interface identifier which is used in extended error reporting.

    If *iid* is not specified, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised if the COM method
    call fails. If *iid* is specified, a [`COMError`](https://docs.python.org/3/library/ctypes.html#ctypes.COMError "ctypes.COMError") is raised
    instead.

    COM methods use a special calling convention: They require a pointer to
    the COM interface as first argument, in addition to those parameters that
    are specified in the `argtypes` tuple.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Windows

The optional *paramflags* parameter creates foreign function wrappers with much
more functionality than the features described above.

*paramflags* must be a tuple of the same length as [`ar