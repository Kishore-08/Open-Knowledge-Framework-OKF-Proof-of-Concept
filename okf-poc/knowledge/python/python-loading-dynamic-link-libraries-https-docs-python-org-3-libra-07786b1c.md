---
id: python-loading-dynamic-link-libraries-https-docs-python-org-3-libra-07786b1c
type: concept
title: Loading dynamic link libraries[¶](https://docs.python.org/3/library/ctypes.html#loading-dynamic-link-libraries
  "Link to this heading")
description: '`ctypes` exports the [`cdll`](https://docs.python.org/3/library/ctypes.html#ctypes.cdll
  "ctypes.cdll"), and on Windows'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Loading dynamic link libraries[¶](https://docs.python.org/3/library/ctypes.html#loading-dynamic-link-libraries "Link to this heading")

`ctypes` exports the [`cdll`](https://docs.python.org/3/library/ctypes.html#ctypes.cdll "ctypes.cdll"), and on Windows
[`windll`](https://docs.python.org/3/library/ctypes.html#ctypes.windll "ctypes.windll") and [`oledll`](https://docs.python.org/3/library/ctypes.html#ctypes.oledll "ctypes.oledll")
objects, for loading dynamic link libraries.

You load libraries by accessing them as attributes of these objects.
`cdll` loads libraries which export functions using the
standard `cdecl` calling convention, while `windll`
libraries call functions using the `stdcall`
calling convention.
[`oledll`](https://docs.python.org/3/library/ctypes.html#ctypes.oledll "ctypes.oledll") also uses the `stdcall` calling convention, and
assumes the functions return a Windows `HRESULT` error code. The error
code is used to automatically raise an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception when the
function call fails.

Changed in version 3.3: Windows errors used to raise [`WindowsError`](https://docs.python.org/3/library/exceptions.html#WindowsError "WindowsError"), which is now an alias
of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

Here are some examples for Windows. Note that `msvcrt` is the MS standard C
library containing most standard C functions, and uses the `cdecl` calling
convention:

```
>>> from ctypes import *
>>> print(windll.kernel32)
<WinDLL 'kernel32', handle ... at ...>
>>> print(cdll.msvcrt)
<CDLL 'msvcrt', handle ... at ...>
>>> libc = cdll.msvcrt
>>>
```

Windows appends the usual `.dll` file suffix automatically.

Note

Accessing the standard C library through `cdll.msvcrt` will use an
outdated version of the library that may be incompatible with the one
being used by Python. Where possible, use native Python functionality,
or else import and use the `msvcrt` module.

Other systems require the filename *including* the extension to
load a library, so attribute access can not be used to load libraries. Either the
[`LoadLibrary()`](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader.LoadLibrary "ctypes.LibraryLoader.LoadLibrary") method of the dll loaders should be used,
or you should load the library by creating an instance of [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL")
by calling the constructor.

For example, on Linux:

```
>>> cdll.LoadLibrary("libc.so.6")
<CDLL 'libc.so.6', handle ... at ...>
>>> libc = CDLL("libc.so.6")
>>> libc
<CDLL 'libc.so.6', handle ... at ...>
>>>
```

On macOS:

```
>>> cdll.LoadLibrary("libc.dylib")
<CDLL 'libc.dylib', handle ... at ...>
>>> libc = CDLL("libc.dylib")
>>> libc
<CDLL 'libc.dylib', handle ... at ...>
```