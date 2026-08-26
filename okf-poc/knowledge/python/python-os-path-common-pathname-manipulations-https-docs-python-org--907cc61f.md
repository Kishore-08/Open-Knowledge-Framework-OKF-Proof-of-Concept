---
id: python-os-path-common-pathname-manipulations-https-docs-python-org--907cc61f
type: concept
title: '`os.path` — Common pathname manipulations[¶](https://docs.python.org/3/library/o'
description: '**Source code:** [Lib/genericpath.py](https://github.com/python/cpython/tree/3.14/Lib/genericpath.py),
  [Lib/posixpath.py](https://github.com/python/cpython/tree/3.14/Lib/posixpath.py)
  (for POSIX) and'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.path.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `os.path` — Common pathname manipulations[¶](https://docs.python.org/3/library/os.path.html#module-os.path "Link to this heading")

**Source code:** [Lib/genericpath.py](https://github.com/python/cpython/tree/3.14/Lib/genericpath.py), [Lib/posixpath.py](https://github.com/python/cpython/tree/3.14/Lib/posixpath.py) (for POSIX) and
[Lib/ntpath.py](https://github.com/python/cpython/tree/3.14/Lib/ntpath.py) (for Windows).

---

This module implements some useful functions on pathnames. To read or write
files see [`open()`](https://docs.python.org/3/library/functions.html#open "open"), and for accessing the filesystem see the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
module. The path parameters can be passed as strings, or bytes, or any object
implementing the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") protocol.

Unlike a Unix shell, Python does not do any *automatic* path expansions.
Functions such as [`expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser") and [`expandvars()`](https://docs.python.org/3/library/os.path.html#os.path.expandvars "os.path.expandvars") can be invoked
explicitly when an application desires shell-like path expansion. (See also
the [`glob`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.") module.)

See also

The [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths") module offers high-level path objects.

Note

All of these functions accept either only bytes or only string objects as
their parameters. The result is an object of the same type, if a path or
file name is returned.

Note

Since different operating systems have different path name conventions, there
are several versions of this module in the standard library. The
`os.path` module is always the path module suitable for the operating
system Python is running on, and therefore usable for local paths. However,
you can also import and use the individual modules if you want to manipulate
a path that is *always* in one of the different formats. They all have the
same interface:

- `posixpath` for UNIX-style paths
- `ntpath` for Windows paths

Changed in version 3.8: [`exists()`](https://docs.python.org/3/library/os.path.html#os.path.exists "os.path.exists"), [`lexists()`](https://docs.python.org/3/library/os.path.html#os.path.lexists "os.path.lexists"), [`isdir()`](https://docs.python.org/3/library/os.path.html#os.path.isdir "os.path.isdir"), [`isfile()`](https://docs.python.org/3/library/os.path.html#os.path.isfile "os.path.isfile"),
[`islink()`](https://docs.python.org/3/library/os.path.html#os.path.islink "os.path.islink"), and [`ismount()`](https://docs.python.org/3/library/os.path.html#os.path.ismount "os.path.ismount") now return `False` instead of
raising an exception for paths that contain characters or bytes
unrepresentable at the OS level.

os.path.abspath(*path*)[¶](https://docs.python.org/3/library/os.path.html#os.path.abspath "Link to this definition")
:   Return a normalized absolutized version of the pathname *path*. On most
    platforms, this is equivalent to calling `normpath(join(os.getcwd(), path))`.

    On Windows the path is normalized by the operating system,
    therefore the result can differ from `normpath(join(os.getcwd(), path))`.
    A drive-relative path is resolved against the current directory
    of the specified drive, and the drive letter is capitalized.
    Trailing dots and spaces are stripped.
    For example:

    ```
    >>> os.path.abspath('c:spam')
    'C:\\Temp\\spam'
    >>> os.path.abspath('c:/temp/spam. . .')
    'c:\\temp\\spam'
    ```

    See also

    [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join "os.path.join") and [`os.path.normpath()`](https://docs.python.org/3/library/os.path.html#os.