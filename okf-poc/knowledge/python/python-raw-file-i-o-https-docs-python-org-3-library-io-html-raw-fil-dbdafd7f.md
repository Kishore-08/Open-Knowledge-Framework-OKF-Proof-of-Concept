---
id: python-raw-file-i-o-https-docs-python-org-3-library-io-html-raw-fil-dbdafd7f
type: concept
title: Raw File I/O[¶](https://docs.python.org/3/library/io.html#raw-file-i-o "Link
  to this heading")
description: '*class* io.FileIO(*name*, *mode=''r''*, *closefd=True*, *opener=None*)[¶](https://docs.python.org/3/library/io.html#io.FileIO
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Raw File I/O[¶](https://docs.python.org/3/library/io.html#raw-file-i-o "Link to this heading")

*class* io.FileIO(*name*, *mode='r'*, *closefd=True*, *opener=None*)[¶](https://docs.python.org/3/library/io.html#io.FileIO "Link to this definition")
:   A raw binary stream representing an OS-level file containing bytes data. It
    inherits from [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") and implements its low-level access design.
    This means [`write()`](https://docs.python.org/3/library/io.html#io.RawIOBase.write "io.RawIOBase.write") does not guarantee all bytes are written
    and [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read") may read less bytes than requested even when more
    bytes may be present in the underlying file. To get “write all” and
    “read at least” behavior, use [Binary I/O](https://docs.python.org/3/library/io.html#binary-io).

    The *name* can be one of two things:

    - a character string or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object representing the path to the
      file which will be opened. In this case closefd must be `True` (the default)
      otherwise an error will be raised.
    - an integer representing the number of an existing OS-level file descriptor
      to which the resulting `FileIO` object will give access. When the
      FileIO object is closed this fd will be closed as well, unless *closefd*
      is set to `False`.

    The *mode* can be `'r'`, `'w'`, `'x'` or `'a'` for reading
    (default), writing, exclusive creation or appending. The file will be
    created if it doesn’t exist when opened for writing or appending; it will be
    truncated when opened for writing. [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") will be raised if
    it already exists when opened for creating. Opening a file for creating
    implies writing, so this mode behaves in a similar way to `'w'`. Add a
    `'+'` to the mode to allow simultaneous reading and writing.

    A custom opener can be used by passing a callable as *opener*. The underlying
    file descriptor for the file object is then obtained by calling *opener* with
    (*name*, *flags*). *opener* must return an open file descriptor (passing
    [`os.open`](https://docs.python.org/3/library/os.html#os.open "os.open") as *opener* results in functionality similar to passing
    `None`).

    The newly created file is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).

    See the [`open()`](https://docs.python.org/3/library/functions.html#open "open") built-in function for examples on using the *opener*
    parameter.

    Warning

    `FileIO` is a low-level I/O object and members, such as
    [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read") and [`write()`](https://docs.python.org/3/library/io.html#io.RawIOBase.write "io.RawIOBase.write"), need to have their
    return values checked explicitly in a retry loop to implement “write all”
    and “read at least” behavior. High-level I/O objects [Binary I/O](https://docs.python.org/3/library/io.html#binary-io) and
    [Text I/O](https://docs.python.org/3/library/io.html#text-io) implement retry behavior.

    Changed in version 3.3: The *opener* parameter was added.
    The `'x'` mode was added.

    Changed in version 3.4: The file is now non-inheritable.

    `FileIO` provides these data attributes in addition to those from
    [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

    mode[¶](https://docs.python.org/3/library/io.html#io.FileIO.mode "Link to this definition")
    :   The mode as given in the constructor.

    name[¶](https://docs.python.org/3/library/io.html#io.FileIO.name "Link to this definition")
    :   The file n