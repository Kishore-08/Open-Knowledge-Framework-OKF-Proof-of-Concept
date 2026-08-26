---
id: python-finding-shared-libraries-https-docs-python-org-3-library-cty-07786b1c
type: concept
title: Finding shared libraries[¶](https://docs.python.org/3/library/ctypes.html#finding-shared-libraries
  "Link to this heading")
description: When programming in a compiled language, shared libraries are accessed
  when
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Finding shared libraries[¶](https://docs.python.org/3/library/ctypes.html#finding-shared-libraries "Link to this heading")

When programming in a compiled language, shared libraries are accessed when
compiling/linking a program, and when the program is run.

The purpose of the [`find_library()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "ctypes.util.find_library") function is to locate a library in a way
similar to what the compiler or runtime loader does (on platforms with several
versions of a shared library the most recent should be loaded), while the ctypes
library loaders act like when a program is run, and call the runtime loader
directly.

The `ctypes.util` module provides a function which can help to determine
the library to load.

ctypes.util.find\_library(*name*)
:   Try to find a library and return a pathname. *name* is the library name without
    any prefix like *lib*, suffix like `.so`, `.dylib` or version number (this
    is the form used for the posix linker option `-l`). If no library can
    be found, returns `None`.

The exact functionality is system dependent.

On Linux, [`find_library()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "ctypes.util.find_library") tries to run external programs
(`/sbin/ldconfig`, `gcc`, `objdump` and `ld`) to find the library file.
It returns the filename of the library file.

Note that if the output of these programs does not correspond to the dynamic
linker used by Python, the result of this function may be misleading.

Changed in version 3.6: On Linux, the value of the environment variable `LD_LIBRARY_PATH` is used
when searching for libraries, if a library cannot be found by any other means.

Here are some examples:

```
>>> from ctypes.util import find_library
>>> find_library("m")
'libm.so.6'
>>> find_library("c")
'libc.so.6'
>>> find_library("bz2")
'libbz2.so.1.0'
>>>
```

On macOS and Android, [`find_library()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "ctypes.util.find_library") uses the system’s
standard naming schemes and paths to locate the library, and returns a full
pathname if successful:

```
>>> from ctypes.util import find_library
>>> find_library("c")
'/usr/lib/libc.dylib'
>>> find_library("m")
'/usr/lib/libm.dylib'
>>> find_library("bz2")
'/usr/lib/libbz2.dylib'
>>> find_library("AGL")
'/System/Library/Frameworks/AGL.framework/AGL'
>>>
```

On Windows, [`find_library()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "ctypes.util.find_library") searches along the system search path, and
returns the full pathname, but since there is no predefined naming scheme a call
like `find_library("c")` will fail and return `None`.

If wrapping a shared library with `ctypes`, it *may* be better to determine
the shared library name at development time, and hardcode that into the wrapper
module instead of using [`find_library()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "ctypes.util.find_library") to locate the library at runtime.