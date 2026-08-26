---
id: python-high-level-module-interface-https-docs-python-org-3-library--dbdafd7f
type: concept
title: High-level Module Interface[¶](https://docs.python.org/3/library/io.html#high-level-module-interface
  "Link to this heading")
description: io.DEFAULT\_BUFFER\_SIZE[¶](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## High-level Module Interface[¶](https://docs.python.org/3/library/io.html#high-level-module-interface "Link to this heading")

io.DEFAULT\_BUFFER\_SIZE[¶](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "Link to this definition")
:   An int containing the default buffer size used by the module’s buffered I/O
    classes. [`open()`](https://docs.python.org/3/library/functions.html#open "open") uses the file’s blksize (as obtained by
    [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")) if possible.

io.open(*file*, *mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*, *newline=None*, *closefd=True*, *opener=None*)[¶](https://docs.python.org/3/library/io.html#io.open "Link to this definition")
:   This is an alias for the builtin `open()` function.

    This function raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with
    arguments *path*, *mode* and *flags*. The *mode* and *flags*
    arguments may have been modified or inferred from the original call.

io.open\_code(*path*)[¶](https://docs.python.org/3/library/io.html#io.open_code "Link to this definition")
:   Opens the provided file with mode `'rb'`. This function should be used
    when the intent is to treat the contents as executable code.

    *path* should be a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") and an absolute path.

    The behavior of this function may be overridden by an earlier call to the
    [`PyFile_SetOpenCodeHook()`](https://docs.python.org/3/c-api/file.html#c.PyFile_SetOpenCodeHook "PyFile_SetOpenCodeHook"). However, assuming that *path* is a
    [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") and an absolute path, `open_code(path)` should always behave
    the same as `open(path, 'rb')`. Overriding the behavior is intended for
    additional validation or preprocessing of the file.

    Added in version 3.8.

io.text\_encoding(*encoding*, *stacklevel=2*, */*)[¶](https://docs.python.org/3/library/io.html#io.text_encoding "Link to this definition")
:   This is a helper function for callables that use [`open()`](https://docs.python.org/3/library/functions.html#open "open") or
    [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") and have an `encoding=None` parameter.

    This function returns *encoding* if it is not `None`.
    Otherwise, it returns `"locale"` or `"utf-8"` depending on
    [UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode).

    This function emits an [`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") if
    [`sys.flags.warn_default_encoding`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags") is true and *encoding*
    is `None`. *stacklevel* specifies where the warning is emitted.
    For example:

    ```
    def read_text(path, encoding=None):
        encoding = io.text_encoding(encoding)  # stacklevel=2
        with open(path, encoding) as f:
            return f.read()
    ```

    In this example, an [`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") is emitted for the caller of
    `read_text()`.

    See [Text Encoding](https://docs.python.org/3/library/io.html#io-text-encoding) for more information.

    Added in version 3.10.

    Changed in version 3.11: `text_encoding()` returns “utf-8” when UTF-8 mode is enabled and
    *encoding* is `None`.

*exception* io.BlockingIOError[¶](https://docs.python.org/3/library/io.html#io.BlockingIOError "Link to this definition")
:   This is a compatibility alias for the builtin `BlockingIOError`
    exception.

*exception* io.UnsupportedOperation[¶](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "Link to this definition")
:   An exception inheriting [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") and [`ValueError`](https://d