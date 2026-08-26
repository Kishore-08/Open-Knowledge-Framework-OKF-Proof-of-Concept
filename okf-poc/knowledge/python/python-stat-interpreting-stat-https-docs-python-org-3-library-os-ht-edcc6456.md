---
id: python-stat-interpreting-stat-https-docs-python-org-3-library-os-ht-edcc6456
type: concept
title: '`stat` — Interpreting [`stat()`](https://docs.python.org/3/library/os.html#os.st'
description: '**Source code:** [Lib/stat.py](https://github.com/python/cpython/tree/3.14/Lib/stat.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stat.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `stat` — Interpreting [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") results[¶](https://docs.python.org/3/library/stat.html#module-stat "Link to this heading")

**Source code:** [Lib/stat.py](https://github.com/python/cpython/tree/3.14/Lib/stat.py)

---

The `stat` module defines constants and functions for interpreting the
results of [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat"), [`os.fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat") and [`os.lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat") (if they
exist). For complete details about the `stat()`, `fstat()` and
`lstat()` calls, consult the documentation for your system.

Changed in version 3.4: The stat module is backed by a C implementation.

The `stat` module defines the following functions to test for specific file
types:

stat.S\_ISDIR(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISDIR "Link to this definition")
:   Return non-zero if the mode is from a directory.

stat.S\_ISCHR(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISCHR "Link to this definition")
:   Return non-zero if the mode is from a character special device file.

stat.S\_ISBLK(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISBLK "Link to this definition")
:   Return non-zero if the mode is from a block special device file.

stat.S\_ISREG(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISREG "Link to this definition")
:   Return non-zero if the mode is from a regular file.

stat.S\_ISFIFO(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISFIFO "Link to this definition")
:   Return non-zero if the mode is from a FIFO (named pipe).

stat.S\_ISLNK(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISLNK "Link to this definition")
:   Return non-zero if the mode is from a symbolic link.

stat.S\_ISSOCK(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISSOCK "Link to this definition")
:   Return non-zero if the mode is from a socket.

stat.S\_ISDOOR(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISDOOR "Link to this definition")
:   Return non-zero if the mode is from a door.

    Added in version 3.4.

stat.S\_ISPORT(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISPORT "Link to this definition")
:   Return non-zero if the mode is from an event port.

    Added in version 3.4.

stat.S\_ISWHT(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISWHT "Link to this definition")
:   Return non-zero if the mode is from a whiteout.

    Added in version 3.4.

Two additional functions are defined for more general manipulation of the file’s
mode:

stat.S\_IMODE(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_IMODE "Link to this definition")
:   Return the portion of the file’s mode that can be set by
    [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")—that is, the file’s permission bits, plus the sticky
    bit, set-group-id, and set-user-id bits (on systems that support them).

stat.S\_IFMT(*mode*)[¶](https://docs.python.org/3/library/stat.html#stat.S_IFMT "Link to this definition")
:   Return the portion of the file’s mode that describes the file type (used by the
    `S_IS*()` functions above).

Normally, you would use the `os.path.is*()` functions for testing the type
of a file; the functions here are useful when you are doing multiple tests of
the same file and wish to avoid the overhead of the `stat()` system call
for each test. These are also useful when checking for information about a file
that isn’t handled by [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames."), like the tests for block and character
devices.

Example:

```
import os, sys
from stat import *

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callb