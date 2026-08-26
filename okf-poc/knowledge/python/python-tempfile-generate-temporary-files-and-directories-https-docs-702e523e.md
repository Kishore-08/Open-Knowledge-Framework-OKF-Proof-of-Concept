---
id: python-tempfile-generate-temporary-files-and-directories-https-docs-702e523e
type: concept
title: '`tempfile` — Generate temporary files and directories[¶](https://docs.python.org'
description: '**Source code:** [Lib/tempfile.py](https://github.com/python/cpython/tree/3.14/Lib/tempfile.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tempfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `tempfile` — Generate temporary files and directories[¶](https://docs.python.org/3/library/tempfile.html#module-tempfile "Link to this heading")

**Source code:** [Lib/tempfile.py](https://github.com/python/cpython/tree/3.14/Lib/tempfile.py)

---

This module creates temporary files and directories. It works on all
supported platforms. [`TemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryFile "tempfile.TemporaryFile"), [`NamedTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile "tempfile.NamedTemporaryFile"),
[`TemporaryDirectory`](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory "tempfile.TemporaryDirectory"), and [`SpooledTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.SpooledTemporaryFile "tempfile.SpooledTemporaryFile") are high-level
interfaces which provide automatic cleanup and can be used as
[context managers](https://docs.python.org/3/glossary.html#term-context-manager). [`mkstemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp "tempfile.mkstemp") and
[`mkdtemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp") are lower-level functions which require manual cleanup.

All the user-callable functions and constructors take additional arguments which
allow direct control over the location and name of temporary files and
directories. Files names used by this module include a string of
random characters which allows those files to be securely created in
shared temporary directories.
To maintain backward compatibility, the argument order is somewhat odd; it
is recommended to use keyword arguments for clarity.

The module defines the following user-callable items:

tempfile.TemporaryFile(*mode='w+b'*, *buffering=-1*, *encoding=None*, *newline=None*, *suffix=None*, *prefix=None*, *dir=None*, *\**, *errors=None*)[¶](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryFile "Link to this definition")
:   Return a [file-like object](https://docs.python.org/3/glossary.html#term-file-like-object) that can be used as a temporary storage area.
    The file is created securely, using the same rules as [`mkstemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp "tempfile.mkstemp"). It will be destroyed as soon
    as it is closed (including an implicit close when the object is garbage
    collected). Under Unix, the directory entry for the file is either not created at all or is removed
    immediately after the file is created. Other platforms do not support
    this; your code should not rely on a temporary file created using this
    function having or not having a visible name in the file system.

    The resulting object can be used as a [context manager](https://docs.python.org/3/glossary.html#term-context-manager) (see
    [Examples](https://docs.python.org/3/library/tempfile.html#tempfile-examples)). On completion of the context or
    destruction of the file object the temporary file will be removed
    from the filesystem.

    The *mode* parameter defaults to `'w+b'` so that the file created can
    be read and written without being closed. Binary mode is used so that it
    behaves consistently on all platforms without regard for the data that is
    stored. *buffering*, *encoding*, *errors* and *newline* are interpreted as for
    [`open()`](https://docs.python.org/3/library/functions.html#open "open").

    The *dir*, *prefix* and *suffix* parameters have the same meaning and
    defaults as with [`mkstemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp "tempfile.mkstemp").

    The returned object is a true file object on POSIX platforms. On other
    platforms, it is a file-like object whose `file` attribute is the
    underlying true file object.

    The [`os.O_TMPFILE`](https://docs.python.org/3/library/os.html#os.O_TMPFILE "os.O_TMPFILE") flag is used if it is available and works