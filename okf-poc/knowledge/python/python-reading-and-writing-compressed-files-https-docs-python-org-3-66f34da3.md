---
id: python-reading-and-writing-compressed-files-https-docs-python-org-3-66f34da3
type: concept
title: Reading and writing compressed files[¶](https://docs.python.org/3/library/compression.zstd.html#reading-and-writing-compressed-files
  "Link to this heading")
description: compression.zstd.open(*file*, */*, *mode='rb'*, *\**, *level=None*, *options=None*,
  *zstd\_dict=None*, *encoding=None*, *errors=None*, *newline=None*)[¶](https://docs.python.org/3/library/compression.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/compression.zstd.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Reading and writing compressed files[¶](https://docs.python.org/3/library/compression.zstd.html#reading-and-writing-compressed-files "Link to this heading")

compression.zstd.open(*file*, */*, *mode='rb'*, *\**, *level=None*, *options=None*, *zstd\_dict=None*, *encoding=None*, *errors=None*, *newline=None*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.open "Link to this definition")
:   Open a Zstandard-compressed file in binary or text mode, returning a
    [file object](https://docs.python.org/3/glossary.html#term-file-object).

    The *file* argument can be either a file name (given as a
    [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [path-like](https://docs.python.org/3/glossary.html#term-path-like-object)
    object), in which case the named file is opened, or it can be an existing
    file object to read from or write to.

    The mode argument can be either `'rb'` for reading (default), `'wb'` for
    overwriting, `'ab'` for appending, or `'xb'` for exclusive creation.
    These can equivalently be given as `'r'`, `'w'`, `'a'`, and `'x'`
    respectively. You may also open in text mode with `'rt'`, `'wt'`,
    `'at'`, and `'xt'` respectively.

    When reading, the *options* argument can be a dictionary providing advanced
    decompression parameters; see [`DecompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter "compression.zstd.DecompressionParameter") for detailed
    information about supported
    parameters. The *zstd\_dict* argument is a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict") instance to be
    used during decompression. When reading, if the *level*
    argument is not None, a `TypeError` will be raised.

    When writing, the *options* argument can be a dictionary
    providing advanced compression parameters; see
    [`CompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter") for detailed information about supported
    parameters. The *level* argument is the compression level to use when
    writing compressed data. Only one of *level* or *options* may be non-None.
    The *zstd\_dict* argument is a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict") instance to be used during
    compression.

    In binary mode, this function is equivalent to the [`ZstdFile`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile "compression.zstd.ZstdFile")
    constructor: `ZstdFile(file, mode, ...)`. In this case, the
    *encoding*, *errors*, and *newline* parameters must not be provided.

    In text mode, a [`ZstdFile`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile "compression.zstd.ZstdFile") object is created, and wrapped in an
    [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") instance with the specified encoding, error
    handling behavior, and line endings.

*class* compression.zstd.ZstdFile(*file*, */*, *mode='rb'*, *\**, *level=None*, *options=None*, *zstd\_dict=None*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile "Link to this definition")
:   Open a Zstandard-compressed file in binary mode.

    A `ZstdFile` can wrap an already-open [file object](https://docs.python.org/3/glossary.html#term-file-object), or operate
    directly on a named file. The *file* argument specifies either the file
    object to wrap, or the name of the file to open (as a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"),
    [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [path-like](http