---
id: python-de-compression-of-files-https-docs-python-org-3-library-bz2--6a582c87
type: concept
title: (De)compression of files[¶](https://docs.python.org/3/library/bz2.html#de-compression-of-files
  "Link to this heading")
description: bz2.open(*filename*, *mode='rb'*, *compresslevel=9*, *encoding=None*,
  *errors=None*, *newline=None*)[¶](https://docs.python.org/3/library/bz2.html#bz2.open
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/bz2.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## (De)compression of files[¶](https://docs.python.org/3/library/bz2.html#de-compression-of-files "Link to this heading")

bz2.open(*filename*, *mode='rb'*, *compresslevel=9*, *encoding=None*, *errors=None*, *newline=None*)[¶](https://docs.python.org/3/library/bz2.html#bz2.open "Link to this definition")
:   Open a bzip2-compressed file in binary or text mode, returning a [file
    object](https://docs.python.org/3/glossary.html#term-file-object).

    As with the constructor for [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File"), the *filename* argument can be
    an actual filename (a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object), or an existing
    file object to read from or write to.

    The *mode* argument can be any of `'r'`, `'rb'`, `'w'`, `'wb'`,
    `'x'`, `'xb'`, `'a'` or `'ab'` for binary mode, or `'rt'`,
    `'wt'`, `'xt'`, or `'at'` for text mode. The default is `'rb'`.

    The *compresslevel* argument is an integer from 1 to 9, as for the
    [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") constructor.

    For binary mode, this function is equivalent to the [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File")
    constructor: `BZ2File(filename, mode, compresslevel=compresslevel)`. In
    this case, the *encoding*, *errors* and *newline* arguments must not be
    provided.

    For text mode, a [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") object is created, and wrapped in an
    [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") instance with the specified encoding, error
    handling behavior, and line ending(s).

    Added in version 3.3.

    Changed in version 3.4: The `'x'` (exclusive creation) mode was added.

    Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

*class* bz2.BZ2File(*filename*, *mode='r'*, *\**, *compresslevel=9*)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "Link to this definition")
:   Open a bzip2-compressed file in binary mode.

    If *filename* is a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object, open the named file
    directly. Otherwise, *filename* should be a [file object](https://docs.python.org/3/glossary.html#term-file-object), which will
    be used to read or write the compressed data.

    The *mode* argument can be either `'r'` for reading (default), `'w'` for
    overwriting, `'x'` for exclusive creation, or `'a'` for appending. These
    can equivalently be given as `'rb'`, `'wb'`, `'xb'` and `'ab'`
    respectively.

    If *filename* is a file object (rather than an actual file name), a mode of
    `'w'` does not truncate the file, and is instead equivalent to `'a'`.

    If *mode* is `'w'` or `'a'`, *compresslevel* can be an integer between
    `1` and `9` specifying the level of compression: `1` produces the
    least compression, and `9` (default) produces the most compression.

    If *mode* is `'r'`, the input file may be the concatenation of multiple
    compressed streams.

    `BZ2File` provides all of the members specified by the
    [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase"), except for [`detach()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.detach "io.BufferedIOBase.detach")
    and [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate").
    Iteration and the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement are supported.

    `BZ2File` also provides the following methods and attributes:

    peek([*n*])[¶](https://docs.python.org/3/library/bz2.h