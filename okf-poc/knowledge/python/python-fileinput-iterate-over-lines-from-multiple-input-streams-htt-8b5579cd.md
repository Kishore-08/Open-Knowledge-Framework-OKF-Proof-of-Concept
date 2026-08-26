---
id: python-fileinput-iterate-over-lines-from-multiple-input-streams-htt-8b5579cd
type: concept
title: '`fileinput` — Iterate over lines from multiple input streams[¶](https://docs.pyt'
description: '**Source code:** [Lib/fileinput.py](https://github.com/python/cpython/tree/3.14/Lib/fileinput.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/fileinput.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `fileinput` — Iterate over lines from multiple input streams[¶](https://docs.python.org/3/library/fileinput.html#module-fileinput "Link to this heading")

**Source code:** [Lib/fileinput.py](https://github.com/python/cpython/tree/3.14/Lib/fileinput.py)

---

This module implements a helper class and functions to quickly write a
loop over standard input or a list of files. If you just want to read or
write one file see [`open()`](https://docs.python.org/3/library/functions.html#open "open").

The typical use is:

```
import fileinput
for line in fileinput.input(encoding="utf-8"):
    process(line)
```

This iterates over the lines of all files listed in `sys.argv[1:]`, defaulting
to `sys.stdin` if the list is empty. If a filename is `'-'`, it is also
replaced by `sys.stdin` and the optional arguments *mode* and *openhook*
are ignored. To specify an alternative list of filenames, pass it as the
first argument to [`input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input"). A single file name is also allowed.

All files are opened in text mode by default, but you can override this by
specifying the *mode* parameter in the call to [`input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input") or
[`FileInput`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput"). If an I/O error occurs during opening or reading a file,
[`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.

Changed in version 3.3: [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") used to be raised; it is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

If `sys.stdin` is used more than once, the second and further use will return
no lines, except perhaps for interactive use, or if it has been explicitly reset
(e.g. using `sys.stdin.seek(0)`).

Empty files are opened and immediately closed; the only time their presence in
the list of filenames is noticeable at all is when the last file opened is
empty.

Lines are returned with any newlines intact, which means that the last line in
a file may not have one.

You can control how files are opened by providing an opening hook via the
*openhook* parameter to [`fileinput.input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input") or [`FileInput()`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput"). The
hook must be a function that takes two arguments, *filename* and *mode*, and
returns an accordingly opened file-like object. If *encoding* and/or *errors*
are specified, they will be passed to the hook as additional keyword arguments.
This module provides a [`hook_compressed()`](https://docs.python.org/3/library/fileinput.html#fileinput.hook_compressed "fileinput.hook_compressed") to support compressed files.

The following function is the primary interface of this module:

fileinput.input(*files=None*, *inplace=False*, *backup=''*, *\**, *mode='r'*, *openhook=None*, *encoding=None*, *errors=None*)[¶](https://docs.python.org/3/library/fileinput.html#fileinput.input "Link to this definition")
:   Create an instance of the [`FileInput`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput") class. The instance will be used
    as global state for the functions of this module, and is also returned to use
    during iteration. The parameters to this function will be passed along to the
    constructor of the `FileInput` class.

    The [`FileInput`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput") instance can be used as a context manager in the
    [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. In this example, *input* is closed after the
    `with` statement is exited, even if an exception occurs:

    ```
    with fi