---
id: python-lzma-compression-using-the-lzma-algorithm-https-docs-python--266ffa0e
type: concept
title: '`lzma` — Compression using the LZMA algorithm[¶](https://docs.python.org/3/libra'
description: Added in version 3.3.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/lzma.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `lzma` — Compression using the LZMA algorithm[¶](https://docs.python.org/3/library/lzma.html#module-lzma "Link to this heading")

Added in version 3.3.

**Source code:** [Lib/lzma.py](https://github.com/python/cpython/tree/3.14/Lib/lzma.py)

---

This module provides classes and convenience functions for compressing and
decompressing data using the LZMA compression algorithm. Also included is a file
interface supporting the `.xz` and legacy `.lzma` file formats used by the
**xz** utility, as well as raw compressed streams.

The interface provided by this module is very similar to that of the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
module. Note that [`LZMAFile`](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile "lzma.LZMAFile") and [`bz2.BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") are *not*
thread-safe, so if you need to use a single `LZMAFile` instance
from multiple threads, it is necessary to protect it with a lock.

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).

*exception* lzma.LZMAError[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMAError "Link to this definition")
:   This exception is raised when an error occurs during compression or
    decompression, or while initializing the compressor/decompressor state.