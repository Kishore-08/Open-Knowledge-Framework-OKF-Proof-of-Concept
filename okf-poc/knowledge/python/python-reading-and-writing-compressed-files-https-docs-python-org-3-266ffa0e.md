---
id: python-reading-and-writing-compressed-files-https-docs-python-org-3-266ffa0e
type: concept
title: Reading and writing compressed files[¶](https://docs.python.org/3/library/lzma.html#reading-and-writing-compressed-files
  "Link to this heading")
description: lzma.open(*filename*, *mode='rb'*, *\**, *format=None*, *check=-1*, *preset=None*,
  *filters=None*, *encoding=None*, *errors=None*, *newline=None*)[¶](https://docs.python.org/3/library/lzma.html#lzma.o
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/lzma.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Reading and writing compressed files[¶](https://docs.python.org/3/library/lzma.html#reading-and-writing-compressed-files "Link to this heading")

lzma.open(*filename*, *mode='rb'*, *\**, *format=None*, *check=-1*, *preset=None*, *filters=None*, *encoding=None*, *errors=None*, *newline=None*)[¶](https://docs.python.org/3/library/lzma.html#lzma.open "Link to this definition")
:   Open an LZMA-compressed file in binary or text mode, returning a [file
    object](https://docs.python.org/3/glossary.html#term-file-object).

    The *filename* argument can be either an actual file name (given as a
    [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [path-like](https://docs.python.org/3/glossary.html#term-path-like-object) object), in
    which case the named file is opened, or it can be an existing file object
    to read from or write to.

    The *mode* argument can be any of `"r"`, `"rb"`, `"w"`, `"wb"`,
    `"x"`, `"xb"`, `"a"` or `"ab"` for binary mode, or `"rt"`,
    `"wt"`, `"xt"`, or `"at"` for text mode. The default is `"rb"`.

    When opening a file for reading, the *format* and *filters* arguments have
    the same meanings as for [`LZMADecompressor`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor "lzma.LZMADecompressor"). In this case, the *check*
    and *preset* arguments should not be used.

    When opening a file for writing, the *format*, *check*, *preset* and
    *filters* arguments have the same meanings as for [`LZMACompressor`](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor "lzma.LZMACompressor").

    For binary mode, this function is equivalent to the [`LZMAFile`](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile "lzma.LZMAFile")
    constructor: `LZMAFile(filename, mode, ...)`. In this case, the *encoding*,
    *errors* and *newline* arguments must not be provided.

    For text mode, a [`LZMAFile`](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile "lzma.LZMAFile") object is created, and wrapped in an
    [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") instance with the specified encoding, error
    handling behavior, and line ending(s).

    Changed in version 3.4: Added support for the `"x"`, `"xb"` and `"xt"` modes.

    Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

*class* lzma.LZMAFile(*filename=None*, *mode='r'*, *\**, *format=None*, *check=-1*, *preset=None*, *filters=None*)[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile "Link to this definition")
:   Open an LZMA-compressed file in binary mode.

    An `LZMAFile` can wrap an already-open [file object](https://docs.python.org/3/glossary.html#term-file-object), or operate
    directly on a named file. The *filename* argument specifies either the file
    object to wrap, or the name of the file to open (as a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"),
    [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [path-like](https://docs.python.org/3/glossary.html#term-path-like-object) object). When wrapping an
    existing file object, the wrapped file will not be closed when the
    `LZMAFile` is closed.

    The *mode* argument can be either `"r"` for reading (default), `"w"` for
    overwriting, `"x"` for exclusive creation, or `"a"` for appending. These
    can equivalently be given as `"rb"`, `"wb"`, `"xb"` and `"ab"`
    respectively.

    If *filename* is a file object (rather than an actual file name), a mode of
    `"w"` does not truncate the file, and is instead equivalent to `"a"`.

    When opening a file for reading, the input file may be the concatenation of
    multiple separate compressed streams. These are transparently decoded as a
    single logical stream.

    When opening a file for reading, the *format* a