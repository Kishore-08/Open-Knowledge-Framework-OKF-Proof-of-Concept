---
id: python-inheritance-of-file-descriptors-https-docs-python-org-3-libr-e86233c0
type: concept
title: Inheritance of File Descriptors[¶](https://docs.python.org/3/library/os.html#inheritance-of-file-descriptors
  "Link to this heading")
description: Added in version 3.4.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Inheritance of File Descriptors[¶](https://docs.python.org/3/library/os.html#inheritance-of-file-descriptors "Link to this heading")

Added in version 3.4.

A file descriptor has an “inheritable” flag which indicates if the file descriptor
can be inherited by child processes. Since Python 3.4, file descriptors
created by Python are non-inheritable by default.

On UNIX, non-inheritable file descriptors are closed in child processes at the
execution of a new program, other file descriptors are inherited. Note that
non-inheritable file descriptors are still *inherited* by child processes on [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork").

On Windows, non-inheritable handles and file descriptors are closed in child
processes, except for standard streams (file descriptors 0, 1 and 2: stdin, stdout
and stderr), which are always inherited. Using [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl") functions,
all inheritable handles and all inheritable file descriptors are inherited.
Using the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") module, all file descriptors except standard
streams are closed, and inheritable handles are only inherited if the
*close\_fds* parameter is `False`.

On WebAssembly platforms, the file descriptor cannot be modified.

os.get\_inheritable(*fd*, */*)[¶](https://docs.python.org/3/library/os.html#os.get_inheritable "Link to this definition")
:   Get the “inheritable” flag of the specified file descriptor (a boolean).

os.set\_inheritable(*fd*, *inheritable*, */*)[¶](https://docs.python.org/3/library/os.html#os.set_inheritable "Link to this definition")
:   Set the “inheritable” flag of the specified file descriptor.

os.get\_handle\_inheritable(*handle*, */*)[¶](https://docs.python.org/3/library/os.html#os.get_handle_inheritable "Link to this definition")
:   Get the “inheritable” flag of the specified handle (a boolean).

    [Availability](https://docs.python.org/3/library/intro.html#availability): Windows.

os.set\_handle\_inheritable(*handle*, *inheritable*, */*)[¶](https://docs.python.org/3/library/os.html#os.set_handle_inheritable "Link to this definition")
:   Set the “inheritable” flag of the specified handle.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Windows.