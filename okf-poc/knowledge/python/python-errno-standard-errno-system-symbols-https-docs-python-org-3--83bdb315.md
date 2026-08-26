---
id: python-errno-standard-errno-system-symbols-https-docs-python-org-3--83bdb315
type: concept
title: '`errno` — Standard errno system symbols[¶](https://docs.python.org/3/library/err'
description: '---'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/errno.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `errno` — Standard errno system symbols[¶](https://docs.python.org/3/library/errno.html#module-errno "Link to this heading")

---

This module makes available standard `errno` system symbols. The value of each
symbol is the corresponding integer value. The names and descriptions are
borrowed from `linux/include/errno.h`, which should be
all-inclusive.

errno.errorcode[¶](https://docs.python.org/3/library/errno.html#errno.errorcode "Link to this definition")
:   Dictionary providing a mapping from the errno value to the string name in the
    underlying system. For instance, `errno.errorcode[errno.EPERM]` maps to
    `'EPERM'`.

To translate a numeric error code to an error message, use [`os.strerror()`](https://docs.python.org/3/library/os.html#os.strerror "os.strerror").

Of the following list, symbols that are not used on the current platform are not
defined by the module. The specific list of defined symbols is available as
`errno.errorcode.keys()`. Symbols available can include:

errno.EPERM[¶](https://docs.python.org/3/library/errno.html#errno.EPERM "Link to this definition")
:   Operation not permitted. This error is mapped to the exception
    [`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError").

errno.ENOENT[¶](https://docs.python.org/3/library/errno.html#errno.ENOENT "Link to this definition")
:   No such file or directory. This error is mapped to the exception
    [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError").

errno.ESRCH[¶](https://docs.python.org/3/library/errno.html#errno.ESRCH "Link to this definition")
:   No such process. This error is mapped to the exception
    [`ProcessLookupError`](https://docs.python.org/3/library/exceptions.html#ProcessLookupError "ProcessLookupError").

errno.EINTR[¶](https://docs.python.org/3/library/errno.html#errno.EINTR "Link to this definition")
:   Interrupted system call. This error is mapped to the exception
    [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError").

errno.EIO[¶](https://docs.python.org/3/library/errno.html#errno.EIO "Link to this definition")
:   I/O error

errno.ENXIO[¶](https://docs.python.org/3/library/errno.html#errno.ENXIO "Link to this definition")
:   No such device or address

errno.E2BIG[¶](https://docs.python.org/3/library/errno.html#errno.E2BIG "Link to this definition")
:   Arg list too long

errno.ENOEXEC[¶](https://docs.python.org/3/library/errno.html#errno.ENOEXEC "Link to this definition")
:   Exec format error

errno.EBADF[¶](https://docs.python.org/3/library/errno.html#errno.EBADF "Link to this definition")
:   Bad file number

errno.ECHILD[¶](https://docs.python.org/3/library/errno.html#errno.ECHILD "Link to this definition")
:   No child processes. This error is mapped to the exception
    [`ChildProcessError`](https://docs.python.org/3/library/exceptions.html#ChildProcessError "ChildProcessError").

errno.EAGAIN[¶](https://docs.python.org/3/library/errno.html#errno.EAGAIN "Link to this definition")
:   Try again. This error is mapped to the exception [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError").

errno.ENOMEM[¶](https://docs.python.org/3/library/errno.html#errno.ENOMEM "Link to this definition")
:   Out of memory

errno.EACCES[¶](https://docs.python.org/3/library/errno.html#errno.EACCES "Link to this definition")
:   Permission denied. This error is mapped to the exception
    [`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError").

errno.EFAULT[¶](https://docs.python.org/3/library/errno.html#errno.EFAULT "Link to this definition")
:   Bad address

errno.ENOTBLK[¶](https://docs.python.org/3/library/errno.html#errno.ENOTBLK "Link to this definition")
:   Block device required

errno.EBUSY[¶](https://docs.python.org/3/library/errno.html#errno.EBUSY "Link to this d