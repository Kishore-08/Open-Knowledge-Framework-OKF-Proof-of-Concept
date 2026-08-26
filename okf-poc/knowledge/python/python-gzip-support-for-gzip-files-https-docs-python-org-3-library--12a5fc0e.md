---
id: python-gzip-support-for-gzip-files-https-docs-python-org-3-library--12a5fc0e
type: concept
title: '`gzip` — Support for **gzip** files[¶](https://docs.python.org/3/library/gzip.ht'
description: '**Source code:** [Lib/gzip.py](https://github.com/python/cpython/tree/3.14/Lib/gzip.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/gzip.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `gzip` — Support for **gzip** files[¶](https://docs.python.org/3/library/gzip.html#module-gzip "Link to this heading")

**Source code:** [Lib/gzip.py](https://github.com/python/cpython/tree/3.14/Lib/gzip.py)

---

This module provides a simple interface to compress and decompress files just
like the GNU programs **gzip** and **gunzip** would.

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).

The data compression is provided by the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module.

The `gzip` module provides the [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile") class, as well as the
[`open()`](https://docs.python.org/3/library/gzip.html#gzip.open "gzip.open"), [`compress()`](https://docs.python.org/3/library/gzip.html#gzip.compress "gzip.compress") and [`decompress()`](https://docs.python.org/3/library/gzip.html#gzip.decompress "gzip.decompress") convenience functions.
The `GzipFile` class reads and writes **gzip**-format files,
automatically compressing or decompressing the data so that it looks like an
ordinary [file object](https://docs.python.org/3/glossary.html#term-file-object).

Note that additional file formats which can be decompressed by the
**gzip** and **gunzip** programs, such as those produced by
**compress** and **pack**, are not supported by this module.

The module defines the following items:

gzip.open(*filename*, *mode='rb'*, *compresslevel=9*, *encoding=None*, *errors=None*, *newline=None*)[¶](https://docs.python.org/3/library/gzip.html#gzip.open "Link to this definition")
:   Open a gzip-compressed file in binary or text mode, returning a [file
    object](https://docs.python.org/3/glossary.html#term-file-object).

    The *filename* argument can be an actual filename (a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or
    [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object), or an existing file object to read from or write to.

    The *mode* argument can be any of `'r'`, `'rb'`, `'a'`, `'ab'`,
    `'w'`, `'wb'`, `'x'` or `'xb'` for binary mode, or `'rt'`,
    `'at'`, `'wt'`, or `'xt'` for text mode. The default is `'rb'`.

    The *compresslevel* argument is an integer from 0 to 9, as for the
    [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile") constructor.

    For binary mode, this function is equivalent to the [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile")
    constructor: `GzipFile(filename, mode, compresslevel)`. In this case, the
    *encoding*, *errors* and *newline* arguments must not be provided.

    For text mode, a [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile") object is created, and wrapped in an
    [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") instance with the specified encoding, error
    handling behavior, and line ending(s).

    Changed in version 3.3: Added support for *filename* being a file object, support for text mode,
    and the *encoding*, *errors* and *newline* arguments.

    Changed in version 3.4: Added support for the `'x'`, `'xb'` and `'xt'` modes.

    Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

*exception* gzip.BadGzipFile[¶](https://docs.python.org/3/library/gzip.html#gzip.BadGzipFile "Link to this definition")
:   An exception raised for invalid gzip files. It inherits from [`OSError`](https://docs.python.