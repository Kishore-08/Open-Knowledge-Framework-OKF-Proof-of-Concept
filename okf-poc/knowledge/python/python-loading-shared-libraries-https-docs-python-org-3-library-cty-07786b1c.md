---
id: python-loading-shared-libraries-https-docs-python-org-3-library-cty-07786b1c
type: concept
title: Loading shared libraries[¶](https://docs.python.org/3/library/ctypes.html#loading-shared-libraries
  "Link to this heading")
description: There are several ways to load shared libraries into the Python process.
  One
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Loading shared libraries[¶](https://docs.python.org/3/library/ctypes.html#loading-shared-libraries "Link to this heading")

There are several ways to load shared libraries into the Python process. One
way is to instantiate [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL") or one of its subclasses:

*class* ctypes.CDLL(*name*, *mode=DEFAULT\_MODE*, *handle=None*, *use\_errno=False*, *use\_last\_error=False*, *winmode=None*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "Link to this definition")
:   Represents a loaded shared library.

    Functions in this library use the standard C calling convention, and are
    assumed to return int.
    The Python [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) is released before calling any
    function exported by these libraries, and reacquired afterwards.
    For different function behavior, use a subclass: [`OleDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.OleDLL "ctypes.OleDLL"),
    [`WinDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.WinDLL "ctypes.WinDLL"), or [`PyDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL "ctypes.PyDLL").

    If you have an existing [`handle`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL._handle "ctypes.CDLL._handle") to an already
    loaded shared library, it can be passed as the *handle* argument to wrap
    the opened library in a new `CDLL` object.
    In this case, *name* is only used to set the [`_name`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL._name "ctypes.CDLL._name")
    attribute, but it may be adjusted and/or validated.

    If *handle* is `None`, the underlying platform’s *[dlopen(3)](https://manpages.debian.org/dlopen(3))* or
    `LoadLibrary()` function is used to load the library into
    the process, and to get a handle to it.

    *name* is the pathname of the shared library to open.
    If *name* does not contain a path separator, the library is found
    in a platform-specific way.

    On non-Windows systems, *name* can be `None`. In this case,
    `dlopen()` is called with `NULL`, which opens the main program
    as a “library”.
    (Some systems do the same is *name* is empty; `None`/`NULL` is more
    portable.)

    CPython implementation detail

    Since CPython is linked to `libc`, a `None` *name* is often used
    to access the C standard library:

    ```
    >>> printf = ctypes.CDLL(None).printf
    >>> printf.argtypes = [ctypes.c_char_p]
    >>> printf(b"hello\n")
    hello
    6
    ```

    To access the Python C API, prefer [`ctypes.pythonapi`](https://docs.python.org/3/library/ctypes.html#ctypes.pythonapi "ctypes.pythonapi") which
    works across platforms.

    The *mode* parameter can be used to specify how the library is loaded. For
    details, consult the *[dlopen(3)](https://manpages.debian.org/dlopen(3))* manpage. On Windows, *mode* is
    ignored. On posix systems, RTLD\_NOW is always added, and is not
    configurable.

    The *use\_errno* parameter, when set to true, enables a ctypes mechanism that
    allows accessing the system [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.") error number in a safe way.
    `ctypes` maintains a thread-local copy of the system’s `errno`
    variable; if you call foreign functions created with `use_errno=True` then the
    `errno` value before the function call is swapped with the ctypes private
    copy, the same happens immediately after the function call.

    The function [`ctypes.get_errno()`](https://docs.python.org/3/library/ctypes.html#ctypes.get_errno "ctypes.get_errno") returns the value of the ctypes private
    copy, and the function [`ctypes.set_errno()`](https://docs.python.org/3/library/ctypes.html#ctypes.set_errno "ctypes.set_errno") changes the ctypes private copy
    to a new value and returns the former value.

    The *use\_last\_